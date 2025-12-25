# Criteria 4: Inference and Monitoring

## Overview

This folder focuses on deploying machine learning models for inference and monitoring their performance in production. It includes scripts for serving models and monitoring metrics.

## Folder Structure

- **inference.py**: Script for serving machine learning models.
- **prometheus_exporter.py**: Script for exporting metrics to Prometheus.
- **prometheus.yml**: Configuration file for Prometheus.
- **mlruns/**: MLflow tracking directory.
  - Tracks experiments, metrics, and artifacts.

## Purpose

The goal of this folder is to:

- Serve machine learning models for inference.
- Monitor model performance and system metrics using Prometheus.
- Ensure the reliability and scalability of deployed models.

## How to Use

1. Run `inference.py` to serve the model.
2. Use `prometheus_exporter.py` to export metrics.
3. Configure Prometheus using `prometheus.yml`.
4. Monitor metrics using Prometheus and Grafana dashboards.
