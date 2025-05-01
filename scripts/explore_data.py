import os
import pandas as pd
import numpy as np
from pathlib import Path
import logging

def explore_data():
    """Explore Excel files for the fuzzy judge project"""
    logging.info("==== Data Exploration for LLM-as-a-Fuzzy-Judge ====")
    
    # Set the path to the raw data directory
    raw_data_dir = Path('../data/raw')
    if not raw_data_dir.exists():
        raw_data_dir = Path('./data/raw')  # Try alternative path
    
    # Get list of Excel files
    excel_files = list(raw_data_dir.glob('fuzzy.coding.data*.xlsx'))
    logging.info(f"Found {len(excel_files)} Excel files in {raw_data_dir}:")
    for file in excel_files:
        logging.info(f"- {file.name}")
    
    if not excel_files:
        logging.warning("No Excel files found. Please check the path and filenames.")
        return
    
    # Load first Excel file for inspection
    logging.info("\nLoading first file for inspection...")
    first_file = excel_files[0]
    try:
        df = pd.read_excel(first_file)
        logging.info(f"Successfully loaded {first_file.name}: {df.shape[0]} rows, {df.shape[1]} columns")
        
        # Display column information
        logging.info("\nColumns in the file:")
        for i, col in enumerate(df.columns):
            logging.info(f"{i+1}. {col} ({df[col].dtype})")
        
        # Display first few rows
        logging.info("\nFirst 3 rows:")
        logging.info(df.head(3).to_string())
        
        # Fuzzy criteria columns - you'll need to identify these
        logging.info("\n==== Fuzzy Criteria Information ====")
        logging.info("The fuzzy criteria you'll need to identify are:")
        logging.info("- Professionalism (3 levels): Unprofessional, Borderline, Appropriate")
        logging.info("- Medical Relevance (3 levels): Irrelevant, Partially relevant, Relevant")
        logging.info("- Ethical Behavior (5 levels): Dangerous, Unsafe, Questionable, Mostly safe, Safe")
        logging.info("- Contextual Distraction (4 levels): Highly distracting, Moderately distracting, Questionable, Not distracting")
        
        logging.info("\nNext steps:")
        logging.info("1. Identify the text column in your data that contains the interactions")
        logging.info("2. Identify the columns that correspond to each fuzzy criterion")
        logging.info("3. Update the main.py script with these column names")
        
    except Exception as e:
        logging.error(f"Error loading {first_file.name}: {e}")

if __name__ == "__main__":
    explore_data() 