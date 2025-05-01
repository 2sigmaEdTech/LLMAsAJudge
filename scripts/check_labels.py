import os
import pandas as pd
import numpy as np
from pathlib import Path
import logging

def check_labels():
    """Check the unique values in the label columns"""
    logging.info("==== Checking Label Values for Fuzzy Criteria ====")
    
    # Set the path to the raw data directory
    raw_data_dir = Path('./data/raw')
    
    # Get list of Excel files
    excel_files = list(raw_data_dir.glob('fuzzy.coding.data*.xlsx'))
    if not excel_files:
        logging.warning("No Excel files found. Please check the path and filenames.")
        return
    
    # Load and merge all files to get comprehensive label information
    logging.info(f"Loading {len(excel_files)} Excel files...")
    dfs = []
    for file in excel_files:
        try:
            df = pd.read_excel(file)
            dfs.append(df)
            logging.info(f"Loaded {file.name}: {df.shape[0]} rows")
        except Exception as e:
            logging.error(f"Error loading {file.name}: {e}")
    
    if not dfs:
        logging.warning("Failed to load any data files.")
        return
    
    # Combine all dataframes
    merged_df = pd.concat(dfs, ignore_index=True)
    logging.info(f"\nCombined dataset: {merged_df.shape[0]} rows, {merged_df.shape[1]} columns")
    
    # Define label columns based on the exploration script's output
    label_columns = {
        'professionalism': 'Professionalism',
        'relevance': 'Medical Relevance',
        'ethics': 'Ethics',
        'distraction': 'Contextual Distraction'
    }
    
    # Check unique values in each label column
    logging.info("\n==== Unique Values in Label Columns ====")
    for criterion, column in label_columns.items():
        if column in merged_df.columns:
            unique_values = merged_df[column].dropna().unique()
            unique_values.sort() # Sort for clearer output
            logging.info(f"\n{criterion.title()} ({column}):")
            for val in unique_values:
                count = merged_df[column].value_counts().get(val, 0)
                percentage = 100 * count / merged_df[column].count()
                logging.info(f"  - '{val}': {count} occurrences ({percentage:.2f}%)")
        else:
            logging.warning(f"{criterion.title()}: Column '{column}' not found")
    
    # Define the expected mappings based on the project requirements
    expected_mappings = {
        'Professionalism': {
            '1. Unprofessional': 0, 
            '2. Borderline': 1, 
            '3. Appropriate': 2
        },
        'Medical Relevance': {
            '1. Irrelevant': 0, 
            '2. Partially Relevant': 1, 
            '3. Relevant': 2
        },
        'Ethics': {
            '1. Dangerous': 0, 
            '2. Unsafe': 1, 
            '3. Questionable': 2, 
            '4. Mostly Safe': 3, 
            '5. Safe': 4
        },
        'Contextual Distraction': {
            '1. Highly Distracting': 0, 
            '2. Moderately Distracting': 1, 
            '3. Questionable': 2, 
            '4. Not Distracting': 3
        }
    }
    
    # Suggested label mappings based on the observed values
    logging.info("\n==== Suggested Label Mappings ====")
    for column, expected_map in expected_mappings.items():
        if column in merged_df.columns:
            unique_values = merged_df[column].dropna().unique()
            logging.info(f"\n{column} mapping:")
            # Try to match observed values with expected values
            # This is a heuristic approach and may need manual correction
            mapping = {}
            for val in unique_values:
                # Find the closest expected value (exact or approx. match)
                mapped_to = None
                for exp_val, idx in expected_map.items():
                    if val == exp_val or val.lower() == exp_val.lower() or val.replace("relevant", "Relevant") == exp_val:
                        mapped_to = idx
                        break
                    # Try partial match if necessary
                    elif exp_val.split('.')[-1].strip().lower() in val.lower():
                        mapped_to = idx
                
                if mapped_to is not None:
                    mapping[val] = mapped_to
                else:
                    # If no match found, print a warning
                    logging.warning(f"  WARNING: No mapping found for '{val}'")
            
            # Print the suggested mapping
            logging.info(f"  '{column}': {mapping}")
        else:
            logging.warning(f"{column}: Column not found")

if __name__ == "__main__":
    check_labels() 