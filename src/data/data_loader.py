import os
import pandas as pd
import numpy as np
from pathlib import Path

class DataLoader:
    def __init__(self, data_dir):
        """
        Initialize data loader with directory containing raw data files.
        
        Args:
            data_dir: Directory containing raw data files
        """
        self.data_dir = Path(data_dir)
        self.raw_data = None
        
        # Define label column names
        self.text_column = 'User Message'
        self.label_columns = {
            'professionalism': 'Professionalism',
            'relevance': 'Medical Relevance',
            'ethics': 'Ethics',
            'distraction': 'Contextual Distraction'
        }
        
        # Define label mappings (observed label value -> numerical index)
        self.label_mappings = {
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
                '4. Mostly safe': 3, 
                '5. Safe': 4
            },
            'Contextual Distraction': {
                '1. Highly distracting': 0, 
                '2. Moderately distracting': 1, 
                '3. Questionable': 2, 
                '4. Not Distracting': 3
            }
        }
        
        # Store the number of classes for each criterion
        self.num_classes = {
            'professionalism': 3,  # Unprofessional, Borderline, Appropriate
            'relevance': 3,        # Irrelevant, Partially Relevant, Relevant  
            'ethics': 5,           # Dangerous, Unsafe, Questionable, Mostly safe, Safe
            'distraction': 4       # Highly distracting, Moderately distracting, Questionable, Not distracting
        }
        
    def load_excel_files(self, pattern="*.xlsx"):
        """
        Load all Excel files matching the pattern in the data directory.
        
        Args:
            pattern: File pattern to match
            
        Returns:
            Dictionary of DataFrames with filenames as keys
        """
        data_dict = {}
        for file_path in self.data_dir.glob(pattern):
            try:
                df = pd.read_excel(file_path)
                data_dict[file_path.name] = df
                print(f"Loaded {file_path.name}: {df.shape[0]} rows, {df.shape[1]} columns")
            except Exception as e:
                print(f"Error loading {file_path.name}: {e}")
        
        return data_dict
    
    def merge_dataframes(self, data_dict):
        """
        Merge multiple dataframes into a single one with source information.
        
        Args:
            data_dict: Dictionary of DataFrames
            
        Returns:
            Merged DataFrame
        """
        merged_data = []
        
        for file_name, df in data_dict.items():
            df = df.copy()  # Create a copy to avoid SettingWithCopyWarning
            df['source_file'] = file_name
            merged_data.append(df)
            
        if merged_data:
            self.raw_data = pd.concat(merged_data, ignore_index=True)
            return self.raw_data
        else:
            print("No data to merge")
            return None
    
    def preprocess_data(self, df=None, criterion=None):
        """
        Preprocess the data for model training, optionally focusing on a specific criterion.
        
        Args:
            df: DataFrame to preprocess (uses self.raw_data if None)
            criterion: Optional criterion to focus on ('professionalism', 'relevance', 'ethics', 'distraction')
                       If None, all criteria will be processed
            
        Returns:
            Preprocessed DataFrame with numerical labels
        """
        if df is None:
            if self.raw_data is None:
                raise ValueError("No data available. Load data first.")
            df = self.raw_data.copy()
        else:
            df = df.copy()  # Create a copy to avoid modifying the original
        
        # Ensure the text column exists
        if self.text_column not in df.columns:
            raise ValueError(f"Text column '{self.text_column}' not found in the data")
        
        # Basic preprocessing on text column
        df[self.text_column] = df[self.text_column].astype(str).str.strip()
        
        # Handle missing values in the text column
        df = df.dropna(subset=[self.text_column])
        
        # Get the relevant label columns to process
        columns_to_process = []
        if criterion is not None:
            # Process only the specified criterion
            if criterion not in self.label_columns:
                raise ValueError(f"Unknown criterion: {criterion}. Available: {list(self.label_columns.keys())}")
            columns_to_process = [self.label_columns[criterion]]
        else:
            # Process all criteria
            columns_to_process = list(self.label_columns.values())
        
        # Verify all required columns exist
        missing_columns = [col for col in columns_to_process if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Required label columns not found: {missing_columns}")
        
        # Apply numerical label mapping for each column
        for col in columns_to_process:
            # Create a new column with numerical labels
            numeric_col = f"{col}_numeric"
            mapping = self.label_mappings.get(col, {})
            
            if not mapping:
                raise ValueError(f"No mapping defined for column: {col}")
            
            # Apply mapping and handle any unexpected values
            df[numeric_col] = df[col].apply(
                lambda x: mapping.get(x, -1) if pd.notna(x) else -1
            )
            
            # Drop rows with unmapped labels (-1)
            unmapped_count = (df[numeric_col] == -1).sum()
            if unmapped_count > 0:
                print(f"Warning: {unmapped_count} rows with unmapped labels in column '{col}' will be dropped")
                df = df[df[numeric_col] != -1]
        
        return df
    
    def split_data(self, df, criterion=None, test_size=0.2, val_size=0.1, random_state=42):
        """
        Split data into train, validation, and test sets for a specific criterion or all criteria.
        
        Args:
            df: DataFrame to split
            criterion: Optional criterion to focus on ('professionalism', 'relevance', 'ethics', 'distraction')
                       If None, all criteria will be included
            test_size: Proportion of data for test set
            val_size: Proportion of data for validation set
            random_state: Random seed for reproducibility
            
        Returns:
            train_df, val_df, test_df
        """
        from sklearn.model_selection import train_test_split
        
        # Get the relevant label column for the criterion
        if criterion is not None:
            if criterion not in self.label_columns:
                raise ValueError(f"Unknown criterion: {criterion}. Available: {list(self.label_columns.keys())}")
            label_col = f"{self.label_columns[criterion]}_numeric"
            
            # Ensure the numeric label column exists
            if label_col not in df.columns:
                raise ValueError(f"Numeric label column '{label_col}' not found. Run preprocess_data first.")
                
            # Drop rows with missing labels for this criterion
            df = df.dropna(subset=[label_col])
        else:
            # If no specific criterion, require all numeric label columns to be present
            numeric_cols = [f"{col}_numeric" for col in self.label_columns.values()]
            missing_cols = [col for col in numeric_cols if col not in df.columns]
            if missing_cols:
                raise ValueError(f"Numeric label columns not found: {missing_cols}. Run preprocess_data first.")
            
            # Drop rows with any missing numeric labels
            df = df.dropna(subset=numeric_cols)
        
        # First split off the test set
        train_val_df, test_df = train_test_split(df, test_size=test_size, random_state=random_state, stratify=None)
        
        # Then split the remaining data into train and validation
        val_ratio = val_size / (1 - test_size)
        train_df, val_df = train_test_split(train_val_df, test_size=val_ratio, random_state=random_state, stratify=None)
        
        print(f"Train set: {train_df.shape[0]} rows")
        print(f"Validation set: {val_df.shape[0]} rows")
        print(f"Test set: {test_df.shape[0]} rows")
        
        return train_df, val_df, test_df
    
    def save_processed_data(self, train_df, val_df, test_df, output_dir, criterion=None):
        """
        Save processed data splits to disk.
        
        Args:
            train_df: Training data
            val_df: Validation data
            test_df: Test data
            output_dir: Directory to save processed data
            criterion: Optional criterion name to include in filenames
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Add criterion to filenames if specified
        prefix = f"{criterion}_" if criterion else ""
        
        train_df.to_csv(output_dir / f"{prefix}train.csv", index=False)
        val_df.to_csv(output_dir / f"{prefix}val.csv", index=False)
        test_df.to_csv(output_dir / f"{prefix}test.csv", index=False)
        
        print(f"Saved processed data to {output_dir}")
    
    def get_text_column(self):
        """Get the name of the text column."""
        return self.text_column
    
    def get_label_column(self, criterion):
        """Get the name of the label column for a specific criterion."""
        if criterion not in self.label_columns:
            raise ValueError(f"Unknown criterion: {criterion}. Available: {list(self.label_columns.keys())}")
        return f"{self.label_columns[criterion]}_numeric"
    
    def get_num_classes(self, criterion):
        """Get the number of classes for a specific criterion."""
        if criterion not in self.num_classes:
            raise ValueError(f"Unknown criterion: {criterion}. Available: {list(self.num_classes.keys())}")
        return self.num_classes[criterion] 