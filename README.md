# Supervised Fine-Tuning Project

This project provides a framework for fine-tuning pretrained language models for supervised tasks using the labeled data in Excel files.

## Project Structure

```
├── data/
│   ├── raw/              # Original Excel files
│   └── processed/        # Processed and split data (CSV)
├── notebooks/
│   ├── csv_transform.ipynb      # CSV transformation notebook
│   └── data_exploration.ipynb   # Data exploration notebook
├── src/
│   ├── data/             # Data processing utilities
│   ├── models/           # Model definitions and training
│   └── utils/            # Helper functions and visualization
├── main.py               # Main script to run the full pipeline
├── requirements.txt      # Project dependencies
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Setup

1. Install the required packages:

```bash
pip install -r requirements.txt
```

2. Ensure your Excel files are in the `data/raw/` directory.

## Usage

### Data Exploration

The project includes a Jupyter notebook for exploring the data:

```bash
jupyter notebook notebooks/data_exploration.ipynb
```

### CSV Transformation

To transform Excel files to CSV format:

```bash
jupyter notebook notebooks/csv_transform.ipynb
```

### Training and Evaluation

Run the main script to process data, train a model, and evaluate it:

```bash
python main.py --text_col [TEXT_COLUMN] --label_col [LABEL_COLUMN]
```

Command-line arguments:

- `--data_dir`: Directory containing raw data files (default: 'data/raw')
- `--processed_dir`: Directory to save processed data (default: 'data/processed')
- `--output_dir`: Directory to save model outputs (default: 'outputs')
- `--model_name`: Pretrained model name from Hugging Face (default: 'bert-base-uncased')
- `--num_labels`: Number of target labels (default: 2)
- `--batch_size`: Training batch size (default: 8)
- `--epochs`: Number of training epochs (default: 3)
- `--learning_rate`: Learning rate for optimizer (default: 2e-5)
- `--text_col`: Column name for text inputs (default: 'text')
- `--label_col`: Column name for labels (default: 'label')

Example:

```bash
python main.py --model_name "distilbert-base-uncased" --epochs 5 --text_col "content" --label_col "category"
```

## Customization

You can customize the project by:

1. Modifying the `DataLoader` class in `src/data/data_loader.py` to fit your data requirements
2. Extending the `BaseModel` class in `src/models/model.py` for specific model architectures
3. Adding visualization functions in `src/utils/visualization.py`

## Git Version Control

This project has been set up with Git version control but excludes raw data files, processed data, and model outputs to keep the repository size manageable. 

### Raw Data Management

Raw data files are excluded from version control. To share the raw data with collaborators, consider:

1. Using a data versioning system like DVC (Data Version Control)
2. Sharing data via a secure file sharing service
3. Creating a documented process for data acquisition

### First-time Git Setup

If you're setting up a new repository:

```bash
# Initialize the repository (already done)
git init

# Add all files except those in .gitignore
git add .

# Make your first commit
git commit -m "Initial project setup"

# Add a remote repository if needed
git remote add origin <repository-url>
git push -u origin main
```

### .gitignore

The included `.gitignore` file excludes:
- Raw and processed data files
- Model outputs and checkpoints
- Python build artifacts
- Environment files
- IDE-specific files
- Jupyter Notebook checkpoints

## License

This project is provided as-is under the MIT license. 