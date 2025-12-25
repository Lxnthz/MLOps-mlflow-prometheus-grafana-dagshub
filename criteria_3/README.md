# Criteria 3: Workflow and CI/CD

## Overview

This folder focuses on implementing workflows and CI/CD pipelines for machine learning projects. It includes scripts, configurations, and workflows for automating the machine learning lifecycle.

## Folder Structure

- **Workflow-CI/**: Contains scripts and configurations for CI/CD workflows.
  - **MLProject/**: MLflow project directory.
    - `conda.yaml`: Conda environment configuration.
    - `docker.txt`: Docker configuration.
    - `MLProject`: MLflow project file.
    - `modelling.py`: Script for training models.
    - `modelling_tuning.py`: Script for hyperparameter tuning.
    - `requirements.txt`: Dependencies for the project.
    - **insurance_preprocessing/**: Preprocessed datasets.
    - **mlruns/**: MLflow tracking directory.
      - Tracks experiments, metrics, and artifacts.
    - **models/**: Contains saved models.

## Purpose

The goal of this folder is to:

- Automate the machine learning lifecycle using CI/CD workflows.
- Track experiments and manage models using MLflow.
- Ensure reproducibility and scalability of machine learning workflows.

## How to Use

1. Set up the environment using `conda.yaml` or `requirements.txt`.
2. Run the scripts in the `MLProject/` directory.
3. Use the CI/CD workflows to automate training and deployment.
