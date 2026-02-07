# Operational Efficiency Analysis

## Overview
This project analyzes operational efficiency in a simulated manufacturing environment.
The objective is to calculate realistic performance metrics by considering effective production time, machine downtime, and production standards (SPM).

All data used in this project is simulated. The calculations and logic are based on real-world industrial scenarios.

---

## Business Context
In manufacturing operations, operator efficiency is often miscalculated due to:
- Ignoring machine downtime
- Using total shift time instead of effective production time
- Applying inconsistent performance metrics

This analysis addresses these issues by defining clear metrics and applying them consistently across operators and shifts.

---

## Dataset
The dataset represents daily production records with the following attributes:
- Operator ID
- Shift
- Total working time
- Machine downtime
- Standard production rate (SPM)
- Actual produced units

The dataset is stored as a CSV file and is intentionally anonymized and simulated.

---

## Key Metrics
The following metrics are calculated:

- **Effective Production Time (min)**  
  Total working time minus machine downtime.

- **Expected Production (units)**  
  Effective time multiplied by the standard production rate (SPM).

- **Efficiency (%)**  
  Ratio between actual production and expected production.

- **Downtime Percentage (%)**  
  Proportion of downtime relative to total working time.

---

## Technical Approach
- Data loading and validation using reusable Python functions
- Separation of business logic from analysis
- Metric calculations implemented in standalone modules
- Aggregation and comparison of operator performance
- Exploratory analysis performed in Jupyter Notebook

---

## Results Summary
Key insights obtained from the analysis include:
- Significant efficiency variability between operators
- Downtime has a stronger impact on performance than small variations in SPM
- Certain shifts show higher variability, indicating potential operational risks

These findings highlight the importance of focusing on downtime reduction rather than only increasing production speed.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## Project Structure


