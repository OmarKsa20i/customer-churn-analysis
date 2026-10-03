# Day 4 — Feature Preparation

## Features Created

### TenureGroup
Grouped customers based on their tenure.

Groups:
- New: 0–12 months
- Early: 13–24 months
- Established: 25–48 months
- Loyal: 49–72 months

Purpose:
To analyze the relationship between customer tenure and churn.

### ServiceCount
Counts the number of selected services used by each customer.

Services:
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies

Purpose:
To analyze the relationship between the number of services and churn.

## Validation

TenureGroup:
- No missing values
- No unexpected values

ServiceCount:
- Values range from 0 to 6
- No missing values
- No unexpected values

## Final Dataset

Rows: 7,043
Columns: 23

New Features:
- TenureGroup
- ServiceCount