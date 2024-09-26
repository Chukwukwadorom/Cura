import os

#directory structure
directories = [
    "data/raw",
    "data/processed",
    "data/external",
    "notebooks",
    "src",
    "models/blenderbot_model",
    "experiments/logs",
    "scripts",
    "config"
]

#files
files = [
    "notebooks/01_data_exploration.ipynb",
    "notebooks/02_data_cleaning.ipynb",
    "notebooks/03_model_training.ipynb",
    "src/data_preprocessing.py",
    "src/chatbot_model.py",
    "src/evaluate.py",
    "src/utils.py",
    "src/memory_management.py",
    "models/model_weights.h5",
    "experiments/metrics.json",
    "scripts/train.py",
    "scripts/test.py",
    "scripts/deploy.py",
    "scripts/inference.py",
    "config/config.yaml",
    "requirements.txt",
    "Dockerfile",
    "README.md",
    ".gitignore"
]

# Create the directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create the empty files
for file in files:
    open(file, 'a').close()

