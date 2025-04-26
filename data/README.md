# Data Directory for LLM-as-a-Fuzzy-Judge Project

This directory contains both raw data files and processed data for the LLM-as-a-Fuzzy-Judge project, which fine-tunes large language models for clinical evaluation based on fuzzy criteria.

## Directory Structure

```
data/
├── raw/          # Original Excel files with labeled interactions (excluded from Git)
└── processed/    # Processed files for each criterion (excluded from Git)
    ├── professionalism/  # Data for the Professionalism criterion
    ├── relevance/        # Data for the Medical Relevance criterion
    ├── ethics/           # Data for the Ethical Behavior criterion
    └── distraction/      # Data for the Contextual Distraction criterion
```

## Raw Data

The `raw/` directory should contain the Excel files with labeled clinical interactions:

- fuzzy.coding.dataCP.xlsx
- fuzzy.coding.dataCZ.xlsx
- fuzzy.coding.dataDF.xlsx
- fuzzy.coding.dataDW.xlsx
- fuzzy.coding.dataMG.xlsx
- fuzzy.coding.dataMK.xlsx
- fuzzy.coding.dataMS.xlsx

Each file contains interactions labeled with the four fuzzy criteria:

1. **Professionalism**: {1. Unprofessional, 2. Borderline, 3. Appropriate}
2. **Medical Relevance**: {1. Irrelevant, 2. Partially relevant, 3. Relevant}
3. **Ethical Behavior**: {1. Dangerous, 2. Unsafe, 3. Questionable, 4. Mostly safe, 5. Safe}
4. **Contextual Distraction**: {1. Highly distracting, 2. Moderately distracting, 3. Questionable, 4. Not distracting}

**Note**: These files are excluded from Git version control to keep the repository size manageable.

### Obtaining Raw Data

If you've cloned this repository, you'll need to obtain the raw data files separately. Contact the project maintainer or refer to the data acquisition procedure documented in your organization.

## Processed Data

The `processed/` directory contains subdirectories for each criterion, each containing CSV files generated after running the data processing pipeline:

```
processed/
├── professionalism/
│   ├── professionalism_train.csv
│   ├── professionalism_val.csv
│   └── professionalism_test.csv
├── relevance/
│   ├── relevance_train.csv
│   ├── relevance_val.csv
│   └── relevance_test.csv
...
```

These files are generated automatically when running the main script:

```bash
python main.py
```

Or for a specific criterion:

```bash
python main.py --criterion professionalism
```

**Note**: Processed data files are also excluded from Git to avoid duplication and maintain version control on the processing code rather than the data itself.

## Data Preprocessing

The data preprocessing steps include:

1. Converting text label values (e.g., "3. Appropriate") to numerical indices (e.g., 2)
2. Handling missing values
3. Splitting the data into train/validation/test sets
4. Saving the processed data to CSV files

## Data Versioning

For proper data versioning, consider using DVC (Data Version Control) alongside Git:

```bash
# Install DVC
pip install dvc

# Initialize DVC
dvc init

# Add raw data files
dvc add data/raw/*.xlsx

# Set up remote storage
dvc remote add -d myremote s3://mybucket/path
# OR for local storage
dvc remote add -d myremote /path/to/remote

# Push data to remote storage
dvc push
```

This allows version control of the data separate from the code, while maintaining synchronization between data and code versions. 