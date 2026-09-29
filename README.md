# Week 2 — Logistics Data Collection, Cleaning & Preprocessing

This repository contains the complete Week 2 internship submission for logistics data science.

## Objective

The objective is to simulate a professional data preprocessing pipeline for logistics analysis. The project focuses on collecting and profiling a public logistics dataset, identifying data-quality problems, cleaning and transforming the data, detecting outliers, handling missing values, and preparing numerical and categorical features for further analysis and machine learning.

## Week 2 Deliverables

- Data collection simulation
- Data profiling
- Missing-value analysis and treatment
- Duplicate detection and handling
- Date/time conversion
- Categorical data standardization
- Outlier detection using the IQR method
- Outlier treatment methodology
- Standardization using StandardScaler
- Min-Max normalization
- Categorical encoding
- Reproducible preprocessing pipeline
- Post-cleaning validation
- Python preprocessing script
- Jupyter Notebook
- Comprehensive DOC report
- Reflection on the impact of data quality

## Repository Structure

```text
logistics-data-science-week2/
│
├── README.md
├── requirements.txt
│
├── Week_2/
│   ├── Week_2_Logistics_Data_Cleaning_Preprocessing_Report.docx
│   ├── logistics_preprocessing.py
│   └── Week_2_Research_Notes.md
│
├── notebooks/
│   └── Week_2_Logistics_Data_Cleaning_Preprocessing.ipynb
│
└── data/
    └── README.md
```

## Dataset

The project uses:

**DataCo SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS**

Source:
https://data.mendeley.com/datasets/8gx2fvg2k6/5

The raw dataset is not committed to this repository. Download it from the public source and place it locally at:

```text
data/raw/DataCoSupplyChainDataset.csv
```

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

## Preprocessing Workflow

```text
DATA COLLECTION
      ↓
DATA PROFILING
      ↓
DUPLICATE CHECK
      ↓
MISSING-VALUE ANALYSIS
      ↓
DATA TYPE & DATE CLEANING
      ↓
CATEGORICAL STANDARDIZATION
      ↓
OUTLIER DETECTION
      ↓
NORMALIZATION / STANDARDIZATION
      ↓
CATEGORICAL ENCODING
      ↓
POST-CLEANING VALIDATION
      ↓
CLEAN DATASET
```

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Then download the DataCo dataset and place it at:

```text
data/raw/DataCoSupplyChainDataset.csv
```

Run:

```bash
python Week_2/logistics_preprocessing.py
```

Or open:

```text
notebooks/Week_2_Logistics_Data_Cleaning_Preprocessing.ipynb
```

## Important Data-Quality Principle

Data should not be changed automatically without understanding its business meaning. For example, an extreme sales value may be a legitimate bulk order rather than an error. Similarly, repeated order IDs may represent multiple order lines rather than duplicate records.

The project therefore follows the principle:

**Detect → Investigate → Validate → Treat → Document**

## References

- DataCo dataset: https://data.mendeley.com/datasets/8gx2fvg2k6/5
- pandas: https://pandas.pydata.org/docs/
- scikit-learn preprocessing: https://scikit-learn.org/stable/modules/preprocessing.html
- scikit-learn pipelines: https://scikit-learn.org/stable/modules/compose.html
