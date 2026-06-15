import os
import argparse
import pandas as pd
from pathlib import Path
import numpy as np
from sklearn.metrics import cohen_kappa_score, accuracy_score, f1_score
from itertools import combinations
import logging

try:
    import krippendorff
except ImportError:
    krippendorff = None

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

def train_criterion_model(criterion, data_loader, args, merged_data=None):
    """
    Train a model for a specific fuzzy criterion.
    
    Args:
        criterion: The criterion to train for ('professionalism', 'relevance', 'ethics', 'distraction')
        data_loader: DataLoader instance
        args: Command line arguments
        merged_data: DataFrame to use for processing (if provided)
    Returns:
        Path to the saved model
    """
    logging.info(f"\n=== Processing {criterion.title()} Criterion ===")
    
    # Create criterion-specific output directories
    criterion_processed_dir = os.path.join(args.processed_dir, criterion)
    criterion_output_dir = os.path.join(args.output_dir, criterion)
    os.makedirs(criterion_processed_dir, exist_ok=True)
    os.makedirs(criterion_output_dir, exist_ok=True)
    
    # Get the appropriate number of classes for this criterion
    num_classes = data_loader.get_num_classes(criterion)
    logging.info(f"Number of classes for {criterion}: {num_classes}")
    
    # Step 1: Preprocess the data for this criterion
    logging.info(f"Preprocessing data for {criterion}...")
    processed_data = data_loader.preprocess_data(df=merged_data, criterion=criterion)
    logging.info(f"Processed data shape: {processed_data.shape}")
    
    # Step 2: Split the data
    logging.info(f"Splitting data for {criterion}...")
    train_df, val_df, test_df = data_loader.split_data(processed_data, criterion=criterion)
    
    # Step 3: Save processed data
    data_loader.save_processed_data(train_df, val_df, test_df, criterion_processed_dir, criterion=criterion)
    
    # Step 4: Plot label distribution
    label_col = data_loader.get_label_column(criterion)
    if label_col in train_df.columns:
        plot_label_distribution(train_df[label_col], f'{criterion.title()} Training Distribution')
    
    # Step 5: Initialize model
    logging.info(f"\n=== Training model for {criterion.title()} ===")
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
    logging.info(f"\n=== Evaluating {criterion.title()} model ===")
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
    logging.info(f"{criterion.title()} Test Loss: {test_loss:.4f}")
    logging.info(f"{criterion.title()} Test Accuracy: {test_acc:.4f}")
    
    # Step 10: Generate confusion matrix and classification report
    test_texts = test_df[text_col].tolist()
    test_preds, test_confidences = model.predict(test_texts, return_confidence=True)
    test_labels = test_df[label_col].tolist()
    
    # Log the first 10 predictions and their confidences
    logging.info("Sample predictions and confidences:")
    for i in range(min(10, len(test_preds))):
        logging.info(f"Text: {test_texts[i]} | Pred: {test_preds[i]} | Confidence: {test_confidences[i]:.4f}")
    
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
    logging.info(f"Cohen's Kappa: {kappa:.4f}")
    logging.info(f"Mean confidence: {mean_conf:.4f}")
    logging.info(f"Accuracy (recomputed): {acc:.4f}")
    logging.info(f"Weighted F1 score: {weighted_f1:.4f}")
    
    logging.info(f"\n=== {criterion.title()} model saved to {best_model_dir} ===")
    return best_model_dir

def further_finetune_with_prompt(criterion, data_loader, args, prev_model_dir):
    """
    Further fine-tune a previously trained model using prompt engineering.
    """
    logging.info(f"\n=== Further Fine-Tuning {criterion.title()} with Prompt Engineering ===")
    
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
    logging.info(f"=== Further fine-tuned {criterion.title()} model saved to {os.path.join(args.output_dir, criterion, 'best_model')} ===")

def compute_inter_annotator_agreement(data_dict, data_loader):
    """
    Calculate inter-annotator agreement statistics for multi-judge annotation.
    
    Computes Krippendorff's α and Fleiss' κ for each criterion to assess
    the reliability and consistency of annotations across judges.
    
    Args:
        data_dict: Dictionary of DataFrames loaded from Excel files
        data_loader: DataLoader instance with label mappings and class counts
    """
    logging.info("=== Computing Inter-Annotator Agreement Statistics ===")
    try:
        if krippendorff is None:
            logging.warning("krippendorff library not found. Skipping inter-annotator agreement calculation.")
            logging.warning("Install with: pip install krippendorff")
            return
        
        criteria = {
            'professionalism': 'Professionalism',
            'relevance': 'Medical Relevance',
            'ethics': 'Ethics',
            'distraction': 'Contextual Distraction'
        }
        
        iaa_results = {}
        reliability_assessment = {}
        
        for criterion_key, criterion_label in criteria.items():
            logging.info(f"\n--- Analyzing {criterion_key.upper()} ---")
            
            # Extract annotations from all judges for this criterion
            annotations_list = []
            judge_annotations = {}
            judge_to_file = {}
            
            for file_name, df in data_dict.items():
                if criterion_label in df.columns:
                    annotations = df[criterion_label].values
                    judge_name = file_name.replace('fuzzy.coding.data_', '').replace('.xlsx', '')
                    judge_annotations[judge_name] = annotations
                    judge_to_file[judge_name] = file_name
                    annotations_list.append(annotations)
            
            if not annotations_list or len(annotations_list) < 2:
                logging.warning(f"Insufficient judges ({len(annotations_list)}) for {criterion_key}")
                continue
            
            # Map labels to numerical values using data_loader's mappings
            label_mapping = data_loader.label_mappings.get(criterion_label, {})
            mapped_data = {}
            
            for judge_name, annotations in judge_annotations.items():
                mapped_annotations = []
                for label in annotations:
                    if pd.isna(label):
                        mapped_annotations.append(np.nan)
                    elif label in label_mapping:
                        mapped_annotations.append(label_mapping[label])
                    else:
                        mapped_annotations.append(np.nan)
                mapped_data[judge_name] = mapped_annotations
            
            judge_names = sorted(mapped_data.keys())
            num_judges = len(judge_names)
            num_units = len(next(iter(mapped_data.values())))
            
            # Compute Krippendorff's alpha for all available judges and all 5-judge subsets
            alpha_summary = []
            if num_judges < 5:
                logging.warning(f"Only {num_judges} judges available for {criterion_key}; computing alpha for the available judges.")
                try:
                    annotation_matrix = np.array([mapped_data[judge] for judge in judge_names])
                    full_alpha = krippendorff.alpha(annotation_matrix, level_of_measurement='ordinal')
                    alpha_summary.append((tuple(judge_names), full_alpha))
                    logging.info(f"Using judges: {', '.join(judge_to_file[j] for j in judge_names)} | Krippendorff's α: {full_alpha:.4f}")
                    iaa_results[criterion_key] = {'krippendorff_alpha': full_alpha}
                except Exception as e:
                    logging.warning(f"Could not calculate Krippendorff's alpha for {criterion_key}: {e}")
                    iaa_results[criterion_key] = {'krippendorff_alpha': None}
            else:
                all_combinations = list(combinations(judge_names, 5))
                logging.info(f"{len(all_combinations)} five-judge combinations available for {criterion_key}.")
                for combo in all_combinations:
                    try:
                        annotation_matrix = np.array([mapped_data[judge] for judge in combo])
                        alpha_val = krippendorff.alpha(annotation_matrix, level_of_measurement='ordinal')
                        alpha_summary.append((combo, alpha_val))
                        used_files = ', '.join(judge_to_file[j] for j in combo)
                        not_used_files = ', '.join(judge_to_file[j] for j in judge_names if j not in combo)
                        logging.info(f"Used: {used_files} | Not used: {not_used_files} | Krippendorff's α: {alpha_val:.4f}")
                    except Exception as e:
                        logging.warning(f"Could not calculate Krippendorff's alpha for subset {combo} in {criterion_key}: {e}")
                        alpha_summary.append((combo, None))
                
                # Save the top and bottom subset scores for easy inspection
                valid_summaries = [(combo, alpha) for combo, alpha in alpha_summary if alpha is not None]
                if valid_summaries:
                    best_subset, best_alpha = max(valid_summaries, key=lambda x: x[1])
                    worst_subset, worst_alpha = min(valid_summaries, key=lambda x: x[1])
                    logging.info(f"Best 5-judge subset for {criterion_key}: {', '.join(judge_to_file[j] for j in best_subset)} = {best_alpha:.4f}")
                    logging.info(f"Worst 5-judge subset for {criterion_key}: {', '.join(judge_to_file[j] for j in worst_subset)} = {worst_alpha:.4f}")
                
                # Also compute full-set alpha for reference if possible
                try:
                    annotation_matrix = np.array([mapped_data[judge] for judge in judge_names])
                    full_alpha = krippendorff.alpha(annotation_matrix, level_of_measurement='ordinal')
                    iaa_results[criterion_key] = {
                        'krippendorff_alpha': full_alpha,
                        'krippendorff_alpha_5_judge_subsets': alpha_summary
                    }
                    logging.info(f"Full judge set alpha ({num_judges} judges) for {criterion_key}: {full_alpha:.4f}")
                except Exception as e:
                    logging.warning(f"Could not calculate Krippendorff's alpha for full judge set for {criterion_key}: {e}")
                    iaa_results[criterion_key] = {
                        'krippendorff_alpha': None,
                        'krippendorff_alpha_5_judge_subsets': alpha_summary
                    }
            
            # Interpret the full-set Krippendorff's alpha if present
            full_alpha = iaa_results[criterion_key].get('krippendorff_alpha')
            if full_alpha is not None:
                logging.info(f"Krippendorff's α (full judge set): {full_alpha:.4f}")
                if full_alpha >= 0.81:
                    reliability = "Excellent"
                elif full_alpha >= 0.67:
                    reliability = "Good"
                elif full_alpha >= 0.51:
                    reliability = "Moderate"
                else:
                    reliability = "Poor"
                reliability_assessment[criterion_key] = reliability
            else:
                reliability_assessment[criterion_key] = "Unknown"
            
            # # Calculate Fleiss' kappa for multiple raters (requires fixed number of raters)
            # try:
            #     num_judges = len(judge_annotations)
            #     num_units = len(next(iter(judge_annotations.values())))
            #     num_classes = data_loader.num_classes.get(criterion_key, len(label_mapping))
                
            #     # Build contingency table for Fleiss' kappa
            #     # Shape: (num_units, num_classes)
            #     contingency_table = np.zeros((num_units, num_classes))
                
            #     for unit_idx in range(num_units):
            #         for judge_name in sorted(judge_annotations.keys()):
            #             label_value = mapped_data[judge_name][unit_idx]
            #             if not pd.isna(label_value):
            #                 label_value = int(label_value)
            #                 if 0 <= label_value < num_classes:
            #                     contingency_table[unit_idx, label_value] += 1
                
            #     # Calculate Fleiss' kappa
            #     # Formula: (P_o - P_e) / (1 - P_e)
            #     # where P_o is observed agreement and P_e is expected agreement
            #     p_o = np.sum(np.sum(contingency_table * (contingency_table - 1), axis=1)) / (num_units * num_judges * (num_judges - 1))
                
            #     # Expected agreement
            #     n_j = np.sum(contingency_table, axis=0)
            #     p_e = np.sum(n_j * (n_j - 1)) / (num_units * num_judges * (num_judges - 1))
                
            #     if p_e < 1:
            #         fleiss_kappa = (p_o - p_e) / (1 - p_e)
            #     else:
            #         fleiss_kappa = 0.0
                
            #     iaa_results[criterion_key]['fleiss_kappa'] = fleiss_kappa
            #     logging.info(f"Fleiss' κ: {fleiss_kappa:.4f}")
                
            #     # Interpret Fleiss' kappa
            #     if fleiss_kappa >= 0.81:
            #         fleiss_reliability = "Excellent"
            #     elif fleiss_kappa >= 0.61:
            #         fleiss_reliability = "Substantial"
            #     elif fleiss_kappa >= 0.41:
            #         fleiss_reliability = "Moderate"
            #     elif fleiss_kappa >= 0.21:
            #         fleiss_reliability = "Fair"
            #     else:
            #         fleiss_reliability = "Poor"
                
            #     logging.info(f"Fleiss' κ Interpretation: {fleiss_reliability}")
            #     logging.info(f"Number of judges: {num_judges}, Number of units: {num_units}, Number of classes: {num_classes}")
                
            # except Exception as e:
            #     logging.warning(f"Could not calculate Fleiss' kappa for {criterion_key}: {e}")
            #     iaa_results[criterion_key]['fleiss_kappa'] = None
        
        # Summary of inter-annotator agreement
        logging.info("\n=== INTER-ANNOTATOR AGREEMENT SUMMARY ===")
        logging.info("Interpretation guidelines:")
        logging.info("  Krippendorff's α: > 0.81 (Excellent), 0.67-0.81 (Good), 0.51-0.67 (Moderate), < 0.51 (Poor)")
        # logging.info("  Fleiss' κ: > 0.81 (Excellent), 0.61-0.81 (Substantial), 0.41-0.61 (Moderate), 0.21-0.41 (Fair), < 0.21 (Poor)")
        logging.info("\nRAW DATA RELIABILITY ASSESSMENT:")
        for criterion, reliability in reliability_assessment.items():
            alpha_val = iaa_results[criterion].get('krippendorff_alpha', 'N/A')
            # kappa_val = iaa_results[criterion].get('fleiss_kappa', 'N/A')
            logging.info(f"  {criterion.upper()}: Krippendorff's α = {alpha_val if isinstance(alpha_val, str) else f'{alpha_val:.4f}'}, ")
                        # f"Fleiss' κ = {kappa_val if isinstance(kappa_val, str) else f'{kappa_val:.4f}'} [{reliability}]")
        
        logging.info("\nDATA RELIABILITY EXPLANATION:")
        logging.info("  - High inter-annotator agreement (α, κ > 0.67) indicates reliable and consistent annotations across judges.")
        logging.info("  - Moderate agreement (0.51 < α < 0.67) suggests acceptable reliability but may require review of edge cases.")
        logging.info("  - Low agreement (α < 0.51) indicates potential issues: unclear criteria, ambiguous examples, or inconsistent judge interpretation.")
        logging.info("  - These statistics validate the quality of raw data before model training.")
        
    except Exception as e:
        logging.error(f"Error computing inter-annotator agreement: {e}")

def main():
    """Main function to run the full workflow."""
    # Parse arguments
    args = parse_args()
    
    # Create directories if they don't exist
    os.makedirs(args.processed_dir, exist_ok=True)
    os.makedirs(args.output_dir, exist_ok=True)
    
    logging.info("=== Loading data ===")
    # Initialize data loader
    data_loader = DataLoader(args.data_dir)
    
    # Load Excel files
    data_dict = data_loader.load_excel_files(pattern="fuzzy.coding.data*.xlsx")
    
    # Calculate inter-annotator agreement statistics
    # compute_inter_annotator_agreement(data_dict, data_loader)
   
    # Merge and report conflicts first
    merged_data, conflicts_df = data_loader.merge_and_report_conflicts(data_dict, conflict_output_path='conflicts_output.xlsx')
    if merged_data is None or merged_data.empty:
        logging.info("No data available after merging. Exiting.")
        return
    if conflicts_df is not None and not conflicts_df.empty:
        logging.info(f"Conflicting rows found and saved to 'conflicts_output.xlsx'.")
    else:
        logging.info("No conflicts found in the merged data.")
    
    # Save merged data to a new file
    merged_data_file = 'merged_data.xlsx'
    merged_data.to_excel(merged_data_file, index=False)
    logging.info(f"Merged data saved to {merged_data_file}")

    # Read the merged data back in
    merged_data = pd.read_excel(merged_data_file)

    logging.info(f"Merged data shape: {merged_data.shape}")
    
    # Define the criteria to process
    criteria = ['professionalism', 'relevance', 'ethics', 'distraction']
    
    # If a specific criterion is specified, only process that one
    if args.criterion:
        if args.criterion not in criteria:
            logging.error(f"Error: Unknown criterion '{args.criterion}'. Available: {criteria}")
            return
        criteria = [args.criterion]
    
    # Train a model for each criterion
    models = {}
    for criterion in criteria:
        model_path = train_criterion_model(criterion, data_loader, args, merged_data=merged_data)
        models[criterion] = model_path
    
    # Print summary
    logging.info("\n=== Training Summary ===")
    for criterion, model_path in models.items():
        logging.info(f"{criterion.title()} model: {model_path}")
    
    # Further fine-tune with prompt engineering
    for criterion, model_path in models.items():
        further_finetune_with_prompt(criterion, data_loader, args, model_path)
    
    logging.info("\n=== Done! ===")

if __name__ == "__main__":
    # Set up logging to both file and console
    log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler('llm_fuzzy_judge.log', mode='a')
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

    main() 