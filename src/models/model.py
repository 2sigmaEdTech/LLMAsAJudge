import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import numpy as np
from transformers import AutoModelForSequenceClassification, AutoTokenizer, Trainer, TrainingArguments
from sklearn.utils.class_weight import compute_class_weight
import logging

class TextDataset(Dataset):
    """Custom dataset for text classification tasks."""
    
    def __init__(self, texts, labels, tokenizer, max_length=512, prompt_template=None):
        """
        Initialize dataset.
        
        Args:
            texts: List of text inputs
            labels: List of corresponding labels
            tokenizer: Tokenizer to use for encoding
            max_length: Maximum sequence length
            prompt_template: Optional string template for prompt engineering
        """
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.prompt_template = prompt_template
        
    def __len__(self):
        return len(self.texts)
    
    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        
        # Apply prompt engineering if a template is provided
        if self.prompt_template:
            text = self.prompt_template.format(user_message=text)
        
        encoding = self.tokenizer(
            text,
            truncation=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )
        
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(label, dtype=torch.long)
        }

class BaseModel:
    """Base class for supervised fine-tuning models."""
    
    def __init__(self, model_name="bert-base-uncased", num_labels=2, device=None):
        """
        Initialize model with pre-trained weights.
        
        Args:
            model_name: Pre-trained model name or path
            num_labels: Number of target labels
            device: Device to use (cuda/cpu)
        """
        self.model_name = model_name
        self.num_labels = num_labels
        self.device = device or ('cuda' if torch.cuda.is_available() else 'cpu')
        
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        # Fix: Set pad token if missing BEFORE loading the model
        pad_token_added = False
        if self.tokenizer.pad_token is None:
            if self.tokenizer.eos_token is not None:
                self.tokenizer.pad_token = self.tokenizer.eos_token
            else:
                self.tokenizer.add_special_tokens({'pad_token': '[PAD]'})
                pad_token_added = True

        self.model = AutoModelForSequenceClassification.from_pretrained(
            model_name, 
            num_labels=num_labels,
            pad_token_id=self.tokenizer.pad_token_id,
            ignore_mismatched_sizes=True
        )
        if pad_token_added:
            self.model.resize_token_embeddings(len(self.tokenizer))
        self.model.to(self.device)
        
    def prepare_data(self, train_df, val_df=None, text_col='text', label_col='label', batch_size=8, max_length=512, prompt_template=None):
        """
        Prepare data for training.
        
        Args:
            train_df: Training DataFrame
            val_df: Validation DataFrame (optional)
            text_col: Column name for text inputs
            label_col: Column name for labels
            batch_size: Batch size for DataLoader
            max_length: Maximum sequence length for tokenization
            prompt_template: Optional string template for prompt engineering
        
        Returns:
            DataLoader for training (and validation if provided)
        """
        # Prepare training data
        train_texts = train_df[text_col].tolist()
        train_labels = train_df[label_col].tolist()
        train_dataset = TextDataset(train_texts, train_labels, self.tokenizer, max_length=max_length, prompt_template=prompt_template)
        train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        
        # Prepare validation data if provided
        val_loader = None
        if val_df is not None:
            val_texts = val_df[text_col].tolist()
            val_labels = val_df[label_col].tolist()
            val_dataset = TextDataset(val_texts, val_labels, self.tokenizer, max_length=max_length, prompt_template=prompt_template)
            val_loader = DataLoader(val_dataset, batch_size=batch_size)
            
        return train_loader, val_loader
    
    def train(self, train_loader, val_loader=None, epochs=5, learning_rate=2e-5, weight_decay=0.01, output_dir="./outputs", class_weights=None):
        """
        Train the model.
        
        Args:
            train_loader: DataLoader for training data
            val_loader: DataLoader for validation data (optional)
            epochs: Number of training epochs
            learning_rate: Learning rate for optimizer
            weight_decay: Weight decay for regularization
            output_dir: Directory to save model checkpoints
            class_weights: Optional tensor of class weights for imbalanced data
        
        Returns:
            Dictionary of training metrics
        """
        optimizer = optim.AdamW(self.model.parameters(), lr=learning_rate, weight_decay=weight_decay)
        total_steps = len(train_loader) * epochs

        # If class_weights not provided, compute from training data
        if class_weights is None:
            all_labels = []
            for batch in train_loader:
                all_labels.extend(batch['labels'].cpu().numpy())
            class_weights_np = compute_class_weight('balanced', classes=np.arange(self.num_labels), y=all_labels)
            class_weights = torch.tensor(class_weights_np, dtype=torch.float).to(self.device)
        
        # Set up loss function with class weights
        loss_fn = nn.CrossEntropyLoss(weight=class_weights)

        history = {'train_loss': [], 'val_loss': [], 'val_acc': []}
        best_val_loss = float('inf')
        
        for epoch in range(epochs):
            self.model.train()
            train_loss = 0
            
            for batch in train_loader:
                input_ids = batch['input_ids'].to(self.device)
                attention_mask = batch['attention_mask'].to(self.device)
                labels = batch['labels'].to(self.device)
                
                outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
                logits = outputs.logits
                loss = loss_fn(logits, labels)
                
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                
                train_loss += loss.item()
            
            avg_train_loss = train_loss / len(train_loader)
            history['train_loss'].append(avg_train_loss)
            
            if val_loader is not None:
                val_loss, val_acc = self.evaluate(val_loader)
                history['val_loss'].append(val_loss)
                history['val_acc'].append(val_acc)
                
                if val_loss < best_val_loss:
                    best_val_loss = val_loss
                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)
                    self.model.save_pretrained(f"{output_dir}/best_model")
                    self.tokenizer.save_pretrained(f"{output_dir}/best_model")
                
                logging.info(f"Epoch {epoch+1}/{epochs} - Train Loss: {avg_train_loss:.4f} - Val Loss: {val_loss:.4f} - Val Acc: {val_acc:.4f}")
            else:
                logging.info(f"Epoch {epoch+1}/{epochs} - Train Loss: {avg_train_loss:.4f}")
        
        return history
    
    def evaluate(self, val_loader):
        """
        Evaluate the model on validation data.
        
        Args:
            val_loader: DataLoader for validation data
            
        Returns:
            Tuple of (validation loss, accuracy)
        """
        self.model.eval()
        val_loss = 0
        all_preds = []
        all_labels = []
        
        with torch.no_grad():
            for batch in val_loader:
                input_ids = batch['input_ids'].to(self.device)
                attention_mask = batch['attention_mask'].to(self.device)
                labels = batch['labels'].to(self.device)
                
                outputs = self.model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
                loss = outputs.loss
                logits = outputs.logits
                
                val_loss += loss.item()
                
                # Convert logits to predictions
                preds = torch.argmax(logits, dim=1).cpu().numpy()
                labels = labels.cpu().numpy()
                
                all_preds.extend(preds)
                all_labels.extend(labels)
        
        # Calculate metrics
        avg_val_loss = val_loss / len(val_loader)
        accuracy = accuracy_score(all_labels, all_preds)
        
        return avg_val_loss, accuracy
    
    def predict(self, texts, max_length=512, batch_size=8, return_confidence=True, prompt_template=None):
        """
        Make predictions on new texts.
        
        Args:
            texts: List of texts to predict
            max_length: Maximum sequence length for tokenization
            batch_size: Batch size for DataLoader
            return_confidence: If True, also return confidence scores (max softmax probability)
        
        Returns:
            Numpy array of predictions (and confidences if requested)
        """
        self.model.eval()
        dataset = TextDataset(texts, [0] * len(texts), self.tokenizer, max_length=max_length, prompt_template=prompt_template)  # Dummy labels
        loader = DataLoader(dataset, batch_size=batch_size)
        
        all_preds = []
        all_confidences = []
        
        with torch.no_grad():
            for batch in loader:
                input_ids = batch['input_ids'].to(self.device)
                attention_mask = batch['attention_mask'].to(self.device)
                
                outputs = self.model(input_ids=input_ids, attention_mask=attention_mask)
                logits = outputs.logits
                
                preds = torch.argmax(logits, dim=1).cpu().numpy()
                all_preds.extend(preds)
                
                if return_confidence:
                    probs = torch.softmax(logits, dim=1)
                    max_conf = torch.max(probs, dim=1).values.cpu().numpy()
                    all_confidences.extend(max_conf)
        
        if return_confidence:
            return np.array(all_preds), np.array(all_confidences)
        else:
            return np.array(all_preds)
    
    def save_model(self, output_dir):
        """
        Save model and tokenizer.
        
        Args:
            output_dir: Directory to save model
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        self.model.save_pretrained(output_dir)
        self.tokenizer.save_pretrained(output_dir)
        logging.info(f"Model saved to {output_dir}")
    
    def load_model(self, model_dir):
        """
        Load model and tokenizer from directory.
        
        Args:
            model_dir: Directory containing saved model
        """
        self.model = AutoModelForSequenceClassification.from_pretrained(model_dir)
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        self.model.to(self.device)
        logging.info(f"Model loaded from {model_dir}") 