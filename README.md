# Logistics Data Science Internship — Week 1

## Strategic Planning and Data Exploration in Logistics

This repository contains the Week 1 strategic planning work for a logistics data science internship/task.

### Project Objective

The project simulates a logistics operation where the business wants to improve delivery reliability, understand delay drivers, forecast operational workload, segment logistics patterns, and explore route/resource optimization.

### Business Questions

1. What is the current delivery performance?
2. Which shipping modes, regions, categories, or order characteristics are associated with late delivery?
3. Can late-delivery risk be predicted before the delivery outcome is known?
4. Can operational demand be forecasted to support resource planning?
5. Can orders/customers/regions be segmented into meaningful groups?
6. How can vehicle capacity and delivery time windows be incorporated into route optimization?

### KPIs

- On-Time Delivery Rate (OTD)
- Late Delivery Rate
- Average Delivery Cycle Time
- Average Delay Days
- Order/Shipment Volume
- Shipping Cost per Order
- Vehicle Utilization
- Risk Intervention Rate

### Dataset

Primary research dataset:

**DataCo SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS**

Mendeley Data:
https://data.mendeley.com/datasets/8gx2fvg2k6/5

The public dataset is used as a research/analytical proxy. Download the dataset from the official repository rather than committing a potentially large raw CSV to this repository.

### Methodology

The proposed analytical workflow is:

DATA COLLECTION
→ DATA PROFILING
→ DATA CLEANING
→ KPI BASELINE
→ EDA
→ FEATURE ENGINEERING
→ PREDICTIVE MODELING
→ CLUSTERING
→ ROUTE/RESOURCE OPTIMIZATION
→ DECISION SUPPORT
→ MONITORING

### Data Science Techniques

- Descriptive analytics
- Exploratory Data Analysis (EDA)
- Classification for late-delivery risk
- Regression for continuous logistics outcomes
- Forecasting for operational demand
- K-Means clustering for segmentation
- Vehicle Routing Problem with Time Windows (VRPTW)
- Model evaluation and monitoring

### Repository Structure

```text
logistics-data-science-internship/
│
├── README.md
├── requirements.txt
│
├── Week_1/
│   ├── Strategic_Planning_Report.docx
│   ├── logistics_analysis.py
│   └── Week_1_Research_Notes.md
│
├── data/
│   └── README.md
│
└── notebooks/
    └── Week_1_Logistics_Analysis.ipynb
```

### Installation

```bash
pip install -r requirements.txt
```

### Running the Python Analysis

After downloading the DataCo dataset and placing it in the appropriate local data location:

```bash
python Week_1/logistics_analysis.py
```

The script demonstrates data loading, profiling, KPI calculation, exploratory analysis, and machine-learning pipeline patterns. Dataset column names should be verified against the dataset's official variable-description file before full execution.

### Important Modeling Principle

For a pre-delivery prediction system, features must only contain information available at the prediction timestamp. Variables created after delivery can cause target leakage and artificially inflate model performance.

### References

- Mendeley Data — DataCo SMART SUPPLY CHAIN FOR BIG DATA ANALYSIS:
  https://data.mendeley.com/datasets/8gx2fvg2k6/5
- scikit-learn:
  https://scikit-learn.org/
- Google OR-Tools Routing:
  https://developers.google.com/optimization/routing
- Google OR-Tools VRP with Time Windows:
  https://developers.google.com/optimization/routing/vrptw
