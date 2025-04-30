#!/bin/bash
#SBATCH --job-name=llm-fuzzy-judge
#SBATCH --output=logs/llm-fuzzy-judge-%j.out
#SBATCH --error=logs/llm-fuzzy-judge-%j.err
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --mem=32G
#SBATCH --cpus-per-task=4
#SBATCH --time=12:00:00

# Load any necessary modules (adjust as needed for your cluster)
module load anaconda/3.0
module load cuda/11.7.0  # or the CUDA version available on your cluster

# Activate your environment if needed
# source activate your_env_name

# Move to your project directory
cd /home/username/ondemand/LLMAsAJudge

# Run your training script (adjust arguments as needed)
python3 main.py --criterion professionalism --epochs 3 --batch_size 8