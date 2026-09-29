# Week 2 Research Notes — Data Cleaning & Preprocessing

## Objective

Prepare logistics data for reliable analytics and machine learning by systematically profiling, cleaning, transforming, validating, and documenting the dataset.

## Reference Dataset

DataCo SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS

https://data.mendeley.com/datasets/8gx2fvg2k6/5

## Pipeline

1. Preserve raw data
2. Inspect schema
3. Profile missing values
4. Check duplicates
5. Validate dataset grain
6. Standardize categorical values
7. Convert dates
8. Handle missing values
9. Detect outliers
10. Encode categorical variables
11. Scale numerical variables where appropriate
12. Validate the cleaned dataset
13. Save and document the processed output

## Key Principles

### Missing Values
Use median imputation for suitable numerical fields and explicit categories such as `unknown` for appropriate categorical fields. Critical identifiers and target variables should not be blindly imputed.

### Duplicates
Remove exact duplicates only after confirming that repeated order IDs are not legitimate order-line records.

### Outliers
Use the IQR method as a detection mechanism. Investigate extreme observations before removing them because large logistics orders or long delivery times may be legitimate.

### Normalization
Use StandardScaler for standardization or MinMaxScaler for bounded 0–1 scaling when the downstream algorithm is sensitive to feature magnitude.

### Leakage Prevention
Preprocessing for a predictive model must respect the prediction timestamp. Information generated after the outcome must not be used as a feature.

## References

- https://data.mendeley.com/datasets/8gx2fvg2k6/5
- https://pandas.pydata.org/docs/user_guide/
- https://scikit-learn.org/stable/modules/preprocessing.html
- https://scikit-learn.org/stable/modules/compose.html
