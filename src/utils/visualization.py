import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
import logging


def plot_training_history(history):
    """
    Plot training and validation loss/accuracy curves.
    
    Args:
        history: Dictionary containing training metrics
    """
    plt.figure(figsize=(12, 5))
    
    # Plot training & validation loss
    plt.subplot(1, 2, 1)
    plt.plot(history['train_loss'], label='Training Loss')
    if 'val_loss' in history:
        plt.plot(history['val_loss'], label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.title('Training and Validation Loss')
    
    # Plot validation accuracy
    if 'val_acc' in history:
        plt.subplot(1, 2, 2)
        plt.plot(history['val_acc'], label='Validation Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.title('Validation Accuracy')
    
    plt.tight_layout()
    plt.show()


def plot_confusion_matrix(y_true, y_pred, class_names=None):
    """
    Plot confusion matrix for classification results.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        class_names: List of class names (optional)
    """
    cm = confusion_matrix(y_true, y_pred)
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(
        cm, 
        annot=True, 
        fmt='d', 
        cmap='Blues',
        xticklabels=class_names if class_names else 'auto',
        yticklabels=class_names if class_names else 'auto'
    )
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.tight_layout()
    plt.show()


def plot_classification_report(y_true, y_pred, class_names=None):
    """
    Display classification report with metrics.
    
    Args:
        y_true: True labels
        y_pred: Predicted labels
        class_names: List of class names (optional)
    """
    report = classification_report(
        y_true, 
        y_pred, 
        target_names=class_names if class_names else None,
        output_dict=True
    )
    
    # Convert the dictionary to a DataFrame for better visualization
    df_report = pd.DataFrame(report).transpose()
    
    # Round values for better display
    df_report = df_report.round(3)
    
    # Print the report
    logging.info("Classification Report:")
    logging.info(df_report)
    
    # Visualize precision, recall, and f1-score
    metrics_df = df_report.iloc[:-3]  # Exclude the avg rows
    
    plt.figure(figsize=(12, 6))
    
    # Plot precision, recall and f1-score as grouped bar chart
    metrics_df[['precision', 'recall', 'f1-score']].plot(kind='bar', figsize=(12, 6))
    plt.title('Precision, Recall and F1-Score by Class')
    plt.xlabel('Class')
    plt.ylabel('Score')
    plt.ylim(0, 1.0)
    plt.legend(loc='lower right')
    plt.tight_layout()
    plt.show()


def plot_label_distribution(labels, title='Label Distribution'):
    """
    Plot the distribution of labels in a dataset.
    
    Args:
        labels: Array or list of labels
        title: Plot title
    """
    # Count occurrences of each label
    label_counts = pd.Series(labels).value_counts().sort_index()
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=label_counts.index, y=label_counts.values)
    plt.title(title)
    plt.xlabel('Label')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_text_length_distribution(texts, bins=50):
    """
    Plot the distribution of text lengths.
    
    Args:
        texts: List of text strings
        bins: Number of bins for histogram
    """
    # Calculate text lengths
    text_lengths = [len(text.split()) for text in texts]
    
    plt.figure(figsize=(12, 6))
    
    # Plot histogram
    plt.hist(text_lengths, bins=bins, alpha=0.7)
    plt.axvline(x=np.mean(text_lengths), color='r', linestyle='--', label=f'Mean: {np.mean(text_lengths):.1f}')
    plt.axvline(x=np.median(text_lengths), color='g', linestyle='--', label=f'Median: {np.median(text_lengths):.1f}')
    
    plt.title('Text Length Distribution (word count)')
    plt.xlabel('Number of Words')
    plt.ylabel('Frequency')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    # Print summary statistics
    logging.info(f"Min length: {min(text_lengths)}")
    logging.info(f"Max length: {max(text_lengths)}")
    logging.info(f"Mean length: {np.mean(text_lengths):.2f}")
    logging.info(f"Median length: {np.median(text_lengths):.2f}")
    logging.info(f"95th percentile: {np.percentile(text_lengths, 95):.2f}") 