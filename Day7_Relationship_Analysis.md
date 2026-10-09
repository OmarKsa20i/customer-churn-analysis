# Day 7 — Relationship Analysis

## Business questions

1. Does the association between contract type and churn change across tenure groups?
2. Within each contract type, are monthly charges different for customers who churned?
3. How does churn vary with the number of selected support, security, and streaming services?
4. Does the electronic-check churn pattern remain when customers are compared within the same contract type?

## Combined findings

### Contract + tenure group

| Contract | New (0–12 months) | Early (13–24) | Established (25–48) | Loyal (49–72) |
|---|---:|---:|---:|---:|
| Month-to-month | 51.35% (n=1,994) | 37.72% (n=737) | 32.92% (n=802) | 26.02% (n=342) |
| One year | 10.48% (n=124) | 8.12% (n=197) | 10.62% (n=518) | 12.93% (n=634) |
| Two year | 0.00% (n=68) | 0.00% (n=90) | 2.19% (n=274) | 3.33% (n=1,263) |

The tenure gradient is strongest among month-to-month customers: churn declines from **51.35%** in the first year to **26.02%** among customers with 49–72 months. One-year rates stay near 8–13%, and two-year rates remain below 3.4%. Some cells, especially the shorter-tenure two-year groups, contain few customers, so their rates are less stable.

### Monthly charges + contract + churn

| Contract | Stayed: mean / median | Churned: mean / median | Churned n |
|---|---:|---:|---:|
| Month-to-month | $61.46 / $64.95 | $73.02 / $79.05 | 1,655 |
| One year | $62.51 / $64.85 | $85.05 / $95.05 | 166 |
| Two year | $60.01 / $63.30 | $86.78 / $97.28 | 48 |

Within each contract type, churned customers have higher monthly-charge averages and medians. The churned groups for one-year and two-year contracts are much smaller, so their averages are more sensitive to individual customers. Charges may also reflect plan and service mix.

### Service count + churn

Churn is **21.41%** for customers with zero selected services, peaks at **45.76%** for one service, then generally declines to **5.28%** for six services. Zero includes customers without internet service as well as customers who do not have any of the six counted services. Service count therefore does not form a simple dose-response pattern.

### Payment method + contract

Electronic-check customers have the highest churn rate within each contract group:

| Contract | Electronic check | Other methods within same contract |
|---|---:|---:|
| Month-to-month | 53.73% (n=1,850) | 32.64% (n=2,025) |
| One year | 18.44% (n=347) | 9.06% (n=1,126) |
| Two year | 7.74% (n=168) | 2.29% (n=1,527) |

The high overall churn for electronic-check customers is not explained only by their greater representation in month-to-month contracts; a gap remains within all three contract groups.

## Pattern review

| Observed pattern | Interpretation | Causation |
|---|---|---|
| Month-to-month churn falls as tenure increases, while one-year and two-year rates remain much lower. | The combination of no long-term commitment and early tenure identifies a high-risk segment. | This is observational. It does not show that tenure or contract length alone causes churn; contract choice and tenure can reflect customer differences and survivorship. |
| Within each contract type, churned customers have higher monthly charges. | Price-to-value and plan fit may be useful topics to investigate in each contract segment. | Higher charges may reflect selected plans or services; this comparison does not establish a price effect. |
| Churn is highest at one selected service and lower at higher counts, with a separate zero-service group. | Service breadth may mark customer needs or engagement, but the zero group mixes customers with different internet eligibility. | Service adoption is not randomly assigned; the pattern cannot show that adding services would prevent churn. |
| Electronic-check churn is higher than other payment methods within each contract type. | Billing method remains a useful segment for follow-up investigation after a simple contract split. | Payment method may correlate with tenure, billing preferences, or other factors; no causal claim is supported. |

## Reproducible output

Run `python q1.py` to print the combined tables and create `Day7_Relationship_Analysis.png` along with the Day 6 charts.
