# Data Directory

## Overview
This directory is the core of our data-related content for the project. It's organized into subfolders that correspond to different stages and types of data processing. Here's a quick guide to each.

## Subfolders and Files

### `archive data`
- Contains archived datasets and other data files that are not in active use but are retained for historical reference.

### `cleaned data`
- `encoded_kaggleheart.csv`: One-hot encoded dataset from Kaggle, ready for use in machine learning models.
- `processed_kaggleheart.csv`: Cleaned and preprocessed dataset from Kaggle, prepared for analysis and visualization.
- `encoded_rawdata.csv`: Processed dataset with one-hot encoding to demonstrate preprocessing techniques.
- `processed_rawdata.csv`: Dataset derived from raw data that has been decoded, combined, and cleaned, ready for analysis and machine learning.

### `raw data`
- Original datasets in their unprocessed form. The inclusion of raw data is crucial for understanding the integrity of our data sources and to build credibility in the data we are using. It allows us to demonstrate transparently the transformations applied to the data from its original state to its final, analyzed form.

### `SQL database`
- Finalized and structured datasets in a SQL database format, optimized for use in queries and application development.
- `data_storing.ipynb`: Python script to upload datasets to an SQLite3 database, enabling easy access and manipulation for machine learning and analytics.

### Processing Scripts
- `KaggleData_Processing.ipynb`: A Jupyter notebook that documents the process of cleaning and preparing the Kaggle data for analysis.
- `RawData_Processing.ipynb`: A Jupyter notebook showcasing the initial data exploration and preprocessing steps applied to the raw data.

## Contributors
- Data cleaning and preprocessing: Eric
- SQL database setup and management: Prachi
