import os
import argparse
import pandas as pd
from pathlib import Path

from src.data.data_loader import DataLoader
from src.models.model import BaseModel
from src.utils.visualization import (
    plot_training_history, plot_confusion_matrix, 
    plot_classification_report, plot_label_distribution
)

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Supervised fine-tuning project')
    parser.add_argument('--data_dir', type=str, default='data/raw',
                        help='Directory containing raw data files')
    parser.add_argument('--processed_dir', type=str, default='data/processed',
                        help='Directory to save processed data')
    parser.add_argument('--output_dir', type=str, default='outputs',
                        help='Directory to save model outputs')
    parser.add_argument('--model_name', type=str, default='bert-base-uncased',
                        help='Pretrained model name from Hugging Face')
    parser.add_argument('--num_labels', type=int, default=2,
                        help='Number of target labels')
    parser.add_argument('--batch_size', type=int, default=8,
                        help='Training batch size')
    parser.add_argument('--epochs', type=int, default=3,
                        help='Number of training epochs')
    parser.add_argument('--learning_rate', type=float, default=2e-5,
                        help='Learning rate for optimizer')
    parser.add_argument('--text_col', type=str, default='text',
                        help='Column name for text inputs')
    parser.add_argument('--label_col', type=str, default='label',
                        help='Column name for labels')
    
    return parser.parse_args()

def main():
    """Main function to run the full workflow."""
    # Parse arguments
    args = parse_args()
    
    # Create directories if they don't exist
    os.makedirs(args.processed_dir, exist_ok=True)
    os.makedirs(args.output_dir, exist_ok=True)
    
    print("=== Loading and processing data ===")
    # Initialize data loader
    data_loader = DataLoader(args.data_dir)
    
    # Load Excel files
    data_dict = data_loader.load_excel_files(pattern="*.xlsx")
    
    # Merge dataframes
    merged_data = data_loader.merge_dataframes(data_dict)
    
    if merged_data is None or merged_data.empty:
        print("No data available. Exiting.")
        return
    
    print(f"Merged data shape: {merged_data.shape}")
    
    # Preprocess data
    processed_data = data_loader.preprocess_data(merged_data)
    print(f"Processed data shape: {processed_data.shape}")
    
    # Split data
    train_df, val_df, test_df = data_loader.split_data(processed_data)
    
    # Save processed data
    data_loader.save_processed_data(train_df, val_df, test_df, args.processed_dir)
    
    # Plot label distribution
    if args.label_col in train_df.columns:
        plot_label_distribution(train_df[args.label_col], 'Training Label Distribution')
    
    print("\n=== Training model ===")
    # Initialize model
    model = BaseModel(
        model_name=args.model_name,
        num_labels=args.num_labels
    )
    
    # Prepare data for training
    train_loader, val_loader = model.prepare_data(
        train_df, 
        val_df,
        text_col=args.text_col,
        label_col=args.label_col,
        batch_size=args.batch_size
    )
    
    # Train model
    history = model.train(
        train_loader,
        val_loader,
        epochs=args.epochs,
        learning_rate=args.learning_rate,
        output_dir=args.output_dir
    )
    
    # Plot training history
    plot_training_history(history)
    
    print("\n=== Evaluating model ===")
    # Load best model
    model.load_model(os.path.join(args.output_dir, 'best_model'))
    
    # Evaluate on test data
    test_loader, _ = model.prepare_data(
        test_df,
        text_col=args.text_col,
        label_col=args.label_col,
        batch_size=args.batch_size
    )
    
    test_loss, test_acc = model.evaluate(test_loader)
    print(f"Test Loss: {test_loss:.4f}")
    print(f"Test Accuracy: {test_acc:.4f}")
    
    # Get predictions for test data
    test_texts = test_df[args.text_col].tolist()
    test_preds = model.predict(test_texts)
    test_labels = test_df[args.label_col].tolist()
    
    # Plot confusion matrix and classification report
    class_names = [str(i) for i in range(args.num_labels)]
    plot_confusion_matrix(test_labels, test_preds, class_names)
    plot_classification_report(test_labels, test_preds, class_names)
    
    print("\n=== Done! ===")
    print(f"Model saved to {os.path.join(args.output_dir, 'best_model')}")

if __name__ == "__main__":
    main() 