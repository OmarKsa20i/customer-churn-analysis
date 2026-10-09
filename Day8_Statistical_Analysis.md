# Day 8 — Statistical Analysis

## Questions that need statistical evidence

The EDA showed noticeable differences in churn by contract and payment method, and in monthly charges by churn status. The following three comparisons were selected for formal tests. The tests were chosen before reviewing these test statistics; Holm adjustment controls the family-wise error rate across this set of three.

1. Is churn associated with contract type?
2. Is churn associated with payment method?
3. Do customers who churn have a different mean monthly charge from customers who stay?

## Test results

| Question | Test and result | Effect size / difference | Holm-adjusted p-value |
|---|---|---|---:|
| Contract type and churn | Pearson chi-square, χ²(2, N=7,043) = **1,184.60**, p = **5.86 × 10⁻²⁵⁸** | Cramér's V = **0.410** | **1.76 × 10⁻²⁵⁷** |
| Payment method and churn | Pearson chi-square, χ²(3, N=7,043) = **648.14**, p = **3.68 × 10⁻¹⁴⁰** | Cramér's V = **0.303** | **7.36 × 10⁻¹⁴⁰** |
| Monthly charges: churned vs stayed | Welch's t-test, t(4,135.8) = **18.41**, p = **8.59 × 10⁻⁷³** | Mean difference = **+$13.18** for churned customers | **8.59 × 10⁻⁷³** |

The mean monthly charge was **$74.44** for customers who churned and **$61.27** for customers who stayed. Every selected result remains statistically significant after Holm adjustment at **α = 0.05** (all adjusted p-values are below 0.001). The categorical results show substantial association in this sample; the monthly-charge result shows a difference in group means.

For both chi-square tests, the smallest expected cell count exceeded 5, so the usual expected-count condition was met. The test uses one record per customer, and the dataset contains no duplicate customer IDs.

## Why these tests fit

- **Pearson chi-square** tests whether two categorical variables are associated. It was used for contract and payment method against the binary churn outcome. Cramér's V summarizes association strength.
- **Welch's independent-samples t-test** compares mean monthly charges between two separate customer groups without assuming equal variances. It directly answers a question about mean charges and accommodates the unequal group sizes.
- **Holm adjustment** was applied to the three p-values to reduce false positives from this set of multiple tests.

## Interpretation and limitations

- Statistical significance does not mean a relationship is causal or that an intervention will have a useful business effect. This is observational data; contract choice, payment method, tenure, and service mix overlap.
- The t-test concerns means only. Monthly charges vary by plan and service combination, so the group difference does not isolate a price effect.
- Welch's test assumes independent observations and is aimed at mean differences. Its large group sizes make the mean comparison stable, but the data may not be normally distributed.
- The chi-square tests assume independent customers and adequate expected cell counts. They do not adjust for tenure, contract, or other customer characteristics.
- These tests were selected after exploratory analysis. Holm adjustment covers these three selected tests, not every comparison inspected during EDA; results remain exploratory and should be confirmed on new data or in a prespecified model.
- Small p-values can occur with a large sample. Cramér's V and the **$13.18** mean difference help describe the size of the observed differences, but business value still requires follow-up analysis.

## Reproducible output

Install the dependencies with `pip install -r requirements.txt`, then run `python q1.py`. The script prints the test tables, statistics, raw p-values, Holm-adjusted p-values, and effect sizes after the EDA sections.
