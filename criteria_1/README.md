# Criteria 1: Data Preprocessing

## Overview

This folder focuses on the preprocessing of raw data to prepare it for machine learning workflows. It includes scripts and datasets used to clean, transform, and preprocess the data.

## Folder Structure

- **Eksperimen*SML*/**: Contains experiments related to data preprocessing.
  - `insurance_raw.csv`: The raw dataset used for preprocessing.
  - **preprocessing/**: Scripts and outputs for preprocessing.
    - `automate_AlthafRafianto.py`: Automation script for preprocessing tasks.
    - `Eksperimen_AlthafRafianto.ipynb`: Jupyter notebook for preprocessing experiments.
    - **insurance_preprocessing/**: Contains preprocessed datasets.
      - `columns.csv`: Metadata about dataset columns.
      - `insurance_clean.csv`: Cleaned dataset.
      - `insurance_test_preprocessed.csv`: Preprocessed test dataset.
      - `insurance_train_preprocessed.csv`: Preprocessed training dataset.

## Purpose

The goal of this folder is to ensure the data is clean, consistent, and ready for machine learning workflows. It includes:

- Handling missing values.
- Encoding categorical variables.
- Splitting data into training and testing sets.

## How to Use

1. Run the preprocessing scripts in the `preprocessing/` folder.
2. Use the cleaned datasets for further analysis or modeling.
