# Day 3 — Data Cleaning Notes

## 1. Missing Values Found

There were 11 missing values in the `TotalCharges` column after converting it to numeric.

## 2. How They Were Handled

The `TotalCharges` column was converted from string to numeric using `pd.to_numeric()`.

The 11 invalid/empty values became `NaN`. They were not removed or replaced yet.

## 3. Duplicate Rows Found

No duplicate rows were found.

## 4. Data Types Changed

`TotalCharges` was changed from `str` to `float64`.

`SeniorCitizen` remained `int64`, and `Churn` remained `str`.

## 5. Categorical Issues

No unexpected or inconsistent categorical values were found.

The checked columns contained the expected categories.

## 6. Numerical Issues

The values in `tenure`, `MonthlyCharges`, and `TotalCharges` were checked using minimum, maximum, and mean.

The values were within reasonable ranges, and no values were removed as outliers.

## 7. Final Dataset Size

The final dataset contains:

* 7,043 rows
* 21 columns

## 8. Final Data-Quality Status

The dataset has no duplicate rows and the data types are suitable for analysis.

There are still 11 missing values in `TotalCharges` that need to be handled before the final analysis.
