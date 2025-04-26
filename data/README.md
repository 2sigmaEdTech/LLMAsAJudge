# Data Directory

This directory contains both raw data files and processed data for the supervised fine-tuning project.

## Directory Structure

```
data/
├── raw/          # Original Excel files (excluded from Git)
└── processed/    # Processed and split CSV files (excluded from Git)
```

## Raw Data

The `raw/` directory should contain the original Excel files with labeled data:

- fuzzy.coding.dataMS.xlsx
- fuzzy.coding.dataMK.xlsx
- fuzzy.coding.dataMG.xlsx
- fuzzy.coding.dataDW.xlsx
- fuzzy.coding.dataDF.xlsx
- fuzzy.coding.dataCZ.xlsx
- fuzzy.coding.dataCP.xlsx

**Note**: These files are excluded from Git version control to keep the repository size manageable. 

### Obtaining Raw Data

If you've cloned this repository, you'll need to obtain the raw data files separately. Contact the project maintainer or refer to the data acquisition procedure documented in your organization.

## Processed Data

The `processed/` directory will contain the processed CSV files after running the data processing pipeline:

- train.csv
- val.csv
- test.csv

These files are generated automatically when running the main script:

```bash
python main.py
```

**Note**: Processed data files are also excluded from Git to avoid duplication and maintain version control on the processing code rather than the data itself.

## Data Versioning

For proper data versioning, consider using a dedicated tool like DVC (Data Version Control) alongside Git. To set up DVC:

1. Install DVC:
```bash
pip install dvc
```

2. Initialize DVC in the project directory:
```bash
dvc init
```

3. Add raw data files to DVC:
```bash
dvc add data/raw/*.xlsx
```

4. Set up remote storage for the data:
```bash
dvc remote add -d myremote s3://mybucket/path
# OR for local storage
dvc remote add -d myremote /path/to/remote
```

5. Push data to remote storage:
```bash
dvc push
```

This allows version control of the data separate from the code, while maintaining synchronization between data and code versions. 