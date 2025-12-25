# Criteria 2: Model Building and Tuning

## Overview

This folder focuses on building and tuning machine learning models. It includes scripts for training models, hyperparameter tuning, and saving model artifacts.

## Folder Structure

- **Membangun_model/**: Contains scripts and datasets for model building.
  - `modelling.py`: Script for training machine learning models.
  - `modelling_tuning.py`: Script for hyperparameter tuning.
  - `requirements.txt`: Dependencies required for running the scripts.
  - **insurance_preprocessing/**: Preprocessed datasets used for modeling.
    - `columns.csv`: Metadata about dataset columns.
    - `insurance_clean.csv`: Cleaned dataset.
    - `insurance_test_preprocessed.csv`: Preprocessed test dataset.
    - `insurance_train_preprocessed.csv`: Preprocessed training dataset.
  - **MLProject/**: Directory for managing MLflow experiments.
    - **models/**: Contains saved models.
  - **mlruns/**: MLflow tracking directory.
    - Tracks experiments, metrics, and artifacts.

## Purpose

The goal of this folder is to:

- Train machine learning models.
- Optimize model performance through hyperparameter tuning.
- Log experiments and artifacts using MLflow and DagsHub.
- Utilize DagsHub for collaborative experiment tracking and version control.

## How to Use

1. Install dependencies using `requirements.txt`.
2. Run `modelling.py` to train models.
3. Use `modelling_tuning.py` for hyperparameter optimization.
   - Hyperparameter tuning is integrated with MLflow for tracking metrics and parameters.
   - Results are logged to DagsHub for collaborative tracking and versioning.
4. Track experiments in the `mlruns/` directory or on DagsHub.
