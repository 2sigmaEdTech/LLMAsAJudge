# LLM-as-a-Fuzzy-Judge: Fine-Tuning LLM for Clinical Evaluation

This project implements a framework for fine-tuning large language models as clinical evaluation judges using fuzzy logic criteria.

## Project Overview

The LLM-as-a-Fuzzy-Judge project fine-tunes models to evaluate clinical interactions based on four key fuzzy criteria:

1. **Professionalism** (3 levels):
   - 1. Unprofessional
   - 2. Borderline
   - 3. Appropriate

2. **Medical Relevance** (3 levels):
   - 1. Irrelevant
   - 2. Partially relevant
   - 3. Relevant

3. **Ethical Behavior** (5 levels):
   - 1. Dangerous
   - 2. Unsafe
   - 3. Questionable
   - 4. Mostly safe
   - 5. Safe

4. **Contextual Distraction** (4 levels):
   - 1. Highly distracting
   - 2. Moderately distracting
   - 3. Questionable
   - 4. Not distracting

## Project Structure

```
├── data/
│   ├── raw/              # Original Excel files with labeled interactions
│   └── processed/        # Processed data for each criterion (CSV)
├── notebooks/
│   ├── csv_transform.ipynb      # CSV transformation notebook
│   └── data_exploration.ipynb   # Data exploration notebook
├── scripts/              # Helper scripts for data exploration
├── src/
│   ├── data/             # Data processing utilities
│   ├── models/           # Model definitions and training
│   └── utils/            # Helper functions and visualization
├── outputs/              # Trained models and results
│   ├── professionalism/  # Professionalism criterion models
│   ├── relevance/        # Medical Relevance criterion models
│   ├── ethics/           # Ethical Behavior criterion models
│   └── distraction/      # Contextual Distraction criterion models
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

2. Ensure your Excel files with labeled data are in the `data/raw/` directory.

## Usage

### Data Exploration

The project includes scripts for exploring the data:

```bash
python scripts/explore_data.py
python scripts/check_labels.py
```

### Training and Evaluation

Run the main script to process data, train the models for all criteria, and evaluate them:

```bash
python main.py
```

To train a model for a specific criterion only:

```bash
python main.py --criterion professionalism
```

Command-line arguments:

- `--data_dir`: Directory containing raw data files (default: 'data/raw')
- `--processed_dir`: Directory to save processed data (default: 'data/processed')
- `--output_dir`: Directory to save model outputs (default: 'outputs')
- `--model_name`: Pretrained model name from Hugging Face (default: 'bert-base-uncased')
- `--batch_size`: Training batch size (default: 8)
- `--epochs`: Number of training epochs (default: 3)
- `--learning_rate`: Learning rate for optimizer (default: 2e-5)
- `--criterion`: Train model for a specific criterion only ('professionalism', 'relevance', 'ethics', 'distraction')
- `--max_length`: Maximum sequence length for tokenization (default: 128)

Example with custom parameters:

```bash
python main.py --model_name "distilbert-base-uncased" --epochs 5 --max_length 256
```

## Customization

You can customize the project by:

1. Modifying the `DataLoader` class in `src/data/data_loader.py` to adapt to different data formats or criteria
2. Extending the `BaseModel` class in `src/models/model.py` for specific model architectures
3. Adding visualization functions in `src/utils/visualization.py`

## Data Format

The expected Excel file format contains the following key columns:

- `User Message`: The text content to be evaluated
- `Professionalism`: The professionalism rating (e.g., "3. Appropriate")
- `Medical Relevance`: The medical relevance rating (e.g., "2. Partially Relevant")
- `Ethics`: The ethical behavior rating (e.g., "5. Safe")
- `Contextual Distraction`: The contextual distraction rating (e.g., "4. Not Distracting")

## Git Version Control

This project uses Git version control but excludes raw data files to keep the repository manageable. See the `.gitignore` file for details on excluded files.

## License

This project is provided as-is under the MIT license. 