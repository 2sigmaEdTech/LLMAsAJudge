import os
import argparse
import pandas as pd
from pathlib import Path
import numpy as np
from sklearn.metrics import cohen_kappa_score, accuracy_score, f1_score

from src.data.data_loader import DataLoader
from src.models.model import BaseModel
from src.utils.visualization import (
    plot_training_history, plot_confusion_matrix, 
    plot_classification_report, plot_label_distribution
)

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='LLM-as-a-Fuzzy-Judge: Fine-tuning for clinical evaluation')
    parser.add_argument('--data_dir', type=str, default='data/raw',
                        help='Directory containing raw data files')
    parser.add_argument('--processed_dir', type=str, default='data/processed',
                        help='Directory to save processed data')
    parser.add_argument('--output_dir', type=str, default='outputs',
                        help='Directory to save model outputs')
    parser.add_argument('--model_name', type=str, default='bert-base-uncased',
                        help='Pretrained model name from Hugging Face')
    parser.add_argument('--batch_size', type=int, default=8,
                        help='Training batch size')
    parser.add_argument('--epochs', type=int, default=3,
                        help='Number of training epochs')
    parser.add_argument('--learning_rate', type=float, default=2e-5,
                        help='Learning rate for optimizer')
    parser.add_argument('--criterion', type=str, default=None, choices=['professionalism', 'relevance', 'ethics', 'distraction'],
                        help='Train model for a specific criterion only (default: train all)')
    parser.add_argument('--max_length', type=int, default=128,
                        help='Maximum sequence length for tokenization')
    
    return parser.parse_args()

def train_criterion_model(criterion, data_loader, args):
    """
    Train a model for a specific fuzzy criterion.
    
    Args:
        criterion: The criterion to train for ('professionalism', 'relevance', 'ethics', 'distraction')
        data_loader: DataLoader instance
        args: Command line arguments
        
    Returns:
        Path to the saved model
    """
    print(f"\n=== Processing {criterion.title()} Criterion ===")
    
    # Create criterion-specific output directories
    criterion_processed_dir = os.path.join(args.processed_dir, criterion)
    criterion_output_dir = os.path.join(args.output_dir, criterion)
    os.makedirs(criterion_processed_dir, exist_ok=True)
    os.makedirs(criterion_output_dir, exist_ok=True)
    
    # Get the appropriate number of classes for this criterion
    num_classes = data_loader.get_num_classes(criterion)
    print(f"Number of classes for {criterion}: {num_classes}")
    
    # Step 1: Preprocess the data for this criterion
    print(f"Preprocessing data for {criterion}...")
    processed_data = data_loader.preprocess_data(criterion=criterion)
    print(f"Processed data shape: {processed_data.shape}")
    
    # Step 2: Split the data
    print(f"Splitting data for {criterion}...")
    train_df, val_df, test_df = data_loader.split_data(processed_data, criterion=criterion)
    
    # Step 3: Save processed data
    data_loader.save_processed_data(train_df, val_df, test_df, criterion_processed_dir, criterion=criterion)
    
    # Step 4: Plot label distribution
    label_col = data_loader.get_label_column(criterion)
    if label_col in train_df.columns:
        plot_label_distribution(train_df[label_col], f'{criterion.title()} Training Distribution')
    
    # Step 5: Initialize model
    print(f"\n=== Training model for {criterion.title()} ===")
    model = BaseModel(
        model_name=args.model_name,
        num_labels=num_classes
    )
    
    # Step 6: Prepare data for training
    text_col = data_loader.get_text_column()
    if criterion == 'professionalism':
        prompt_template = "Judge the professionalism of this message: '{user_message}'. Answer with Unprofessional, Borderline, or Appropriate."
    elif criterion == 'relevance':
        prompt_template = "Is the following message relevant to the medical context? '{user_message}'"
    elif criterion == 'ethics':
        prompt_template = "Evaluate the ethical implications of this message: '{user_message}'"
    elif criterion == 'distraction':
        prompt_template = "Evaluate the distraction level of this message: '{user_message}'"
    else:
        prompt_template = None
    
    train_loader, val_loader = model.prepare_data(
        train_df, 
        val_df,
        text_col=text_col,
        label_col=label_col,
        batch_size=args.batch_size,
        max_length=args.max_length,
        prompt_template=prompt_template
    )
    
    # Step 7: Train model
    history = model.train(
        train_loader,
        val_loader,
        epochs=args.epochs,
        learning_rate=args.learning_rate,
        output_dir=criterion_output_dir
    )
    
    # Step 8: Plot training history
    plot_training_history(history)
    
    # Step 9: Evaluate on test data
    print(f"\n=== Evaluating {criterion.title()} model ===")
    best_model_dir = os.path.join(criterion_output_dir, 'best_model')
    if os.path.exists(best_model_dir):
        model.load_model(best_model_dir)
    
    test_loader, _ = model.prepare_data(
        test_df,
        text_col=text_col,
        label_col=label_col,
        batch_size=args.batch_size,
        max_length=args.max_length
    )
    
    test_loss, test_acc = model.evaluate(test_loader)
    print(f"{criterion.title()} Test Loss: {test_loss:.4f}")
    print(f"{criterion.title()} Test Accuracy: {test_acc:.4f}")
    
    # Step 10: Generate confusion matrix and classification report
    test_texts = test_df[text_col].tolist()
    test_preds, test_confidences = model.predict(test_texts, return_confidence=True)
    test_labels = test_df[label_col].tolist()
    
    # Log the first 10 predictions and their confidences
    print("Sample predictions and confidences:")
    for i in range(min(10, len(test_preds))):
        print(f"Text: {test_texts[i]} | Pred: {test_preds[i]} | Confidence: {test_confidences[i]:.4f}")
    
    # Use criterion-specific class names
    if criterion == 'professionalism':
        class_names = ['Unprofessional', 'Borderline', 'Appropriate']
    elif criterion == 'relevance':
        class_names = ['Irrelevant', 'Partially relevant', 'Relevant']
    elif criterion == 'ethics':
        class_names = ['Dangerous', 'Unsafe', 'Questionable', 'Mostly safe', 'Safe']
    elif criterion == 'distraction':
        class_names = ['Highly distracting', 'Moderately distracting', 'Questionable', 'Not distracting']
    else:
        class_names = [str(i) for i in range(num_classes)]
        
    plot_confusion_matrix(test_labels, test_preds, class_names)
    plot_classification_report(test_labels, test_preds, class_names)
    
    # Compute and print Cohen's Kappa, mean confidence, accuracy, and weighted F1
    kappa = cohen_kappa_score(test_labels, test_preds)
    mean_conf = float(np.mean(test_confidences))
    acc = accuracy_score(test_labels, test_preds)
    weighted_f1 = f1_score(test_labels, test_preds, average='weighted')
    print(f"Cohen's Kappa: {kappa:.4f}")
    print(f"Mean confidence: {mean_conf:.4f}")
    print(f"Accuracy (recomputed): {acc:.4f}")
    print(f"Weighted F1 score: {weighted_f1:.4f}")
    
    print(f"\n=== {criterion.title()} model saved to {best_model_dir} ===")
    return best_model_dir

def further_finetune_with_prompt(criterion, data_loader, args, prev_model_dir):
    """
    Further fine-tune a previously trained model using prompt engineering.
    """
    print(f"\n=== Further Fine-Tuning {criterion.title()} with Prompt Engineering ===")
    
    # Load processed data
    criterion_processed_dir = os.path.join(args.processed_dir, criterion)
    train_df = pd.read_csv(os.path.join(criterion_processed_dir, f"{criterion}_train.csv"))
    val_df = pd.read_csv(os.path.join(criterion_processed_dir, f"{criterion}_val.csv"))
    
    # Initialize and load previous model
    num_classes = data_loader.get_num_classes(criterion)
    model = BaseModel(model_name=prev_model_dir, num_labels=num_classes)
    model.load_model(prev_model_dir)
    
    # Define prompt template
    if criterion == 'professionalism':
        prompt_template = "Judge the professionalism of this message: '{user_message}'. Answer with Unprofessional, Borderline, or Appropriate."
    elif criterion == 'relevance':
        prompt_template = "Is the following message relevant to the medical context? '{user_message}'"
    elif criterion == 'ethics':
        prompt_template = "Evaluate the ethical implications of this message: '{user_message}'"
    elif criterion == 'distraction':
        prompt_template = "Evaluate the distraction level of this message: '{user_message}'"
    else:
        prompt_template = None

    text_col = data_loader.get_text_column()
    label_col = data_loader.get_label_column(criterion)
    
    # Prepare data with prompt engineering
    train_loader, val_loader = model.prepare_data(
        train_df,
        val_df,
        text_col=text_col,
        label_col=label_col,
        batch_size=args.batch_size,
        max_length=args.max_length,
        prompt_template=prompt_template
    )
    
    # Continue training
    model.train(
        train_loader,
        val_loader,
        epochs=args.epochs,
        learning_rate=args.learning_rate,
        output_dir=os.path.join(args.output_dir, criterion)
    )
    print(f"=== Further fine-tuned {criterion.title()} model saved to {os.path.join(args.output_dir, criterion, 'best_model')} ===")

def main():
    """Main function to run the full workflow."""
    # Parse arguments
    args = parse_args()
    
    # Create directories if they don't exist
    os.makedirs(args.processed_dir, exist_ok=True)
    os.makedirs(args.output_dir, exist_ok=True)
    
    print("=== Loading data ===")
    # Initialize data loader
    data_loader = DataLoader(args.data_dir)
    
    # Load Excel files
    data_dict = data_loader.load_excel_files(pattern="fuzzy.coding.data*.xlsx")
    
    # Merge dataframes
    merged_data = data_loader.merge_dataframes(data_dict)
    
    if merged_data is None or merged_data.empty:
        print("No data available. Exiting.")
        return
    
    print(f"Merged data shape: {merged_data.shape}")
    
    # Define the criteria to process
    criteria = ['professionalism', 'relevance', 'ethics', 'distraction']
    
    # If a specific criterion is specified, only process that one
    if args.criterion:
        if args.criterion not in criteria:
            print(f"Error: Unknown criterion '{args.criterion}'. Available: {criteria}")
            return
        criteria = [args.criterion]
    
    # Train a model for each criterion
    models = {}
    for criterion in criteria:
        model_path = train_criterion_model(criterion, data_loader, args)
        models[criterion] = model_path
    
    # Print summary
    print("\n=== Training Summary ===")
    for criterion, model_path in models.items():
        print(f"{criterion.title()} model: {model_path}")
    
    # Further fine-tune with prompt engineering
    for criterion, model_path in models.items():
        further_finetune_with_prompt(criterion, data_loader, args, model_path)
    
    print("\n=== Done! ===")

if __name__ == "__main__":
    main() 