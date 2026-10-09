# Day 6 — EDA II: Charges, Payment, and Services

## Dataset verification

- **7,043 rows and 21 columns** in the source CSV.
- **1,869 customers churned (26.54%)**; 5,174 stayed (73.46%).
- No duplicate rows or duplicate `customerID` values were found.
- `TotalCharges` has **11 blank values**. All 11 belong to customers with zero months of tenure who did not churn. They were kept as missing and excluded from `TotalCharges` summaries rather than treated as zero.
- No missing values were found in the other source columns.

## Findings linked to business questions

### 1. Are customers who churn paying more each month?

Yes, in this dataset. Churned customers have a median `MonthlyCharges` of **$79.65** and a mean of **$74.44**, compared with **$64.43** and **$61.27** for customers who stayed. Higher monthly bills are a useful segment signal to investigate in pricing, plan fit, and value conversations; this comparison alone does not show that price caused churn.

### 2. Do churned customers have higher lifetime charges?

No. Median `TotalCharges` are **$703.55** for churned customers and **$1,683.60** for customers who stayed; the means are **$1,531.80** and **$2,555.34**, respectively. Churned customers tend to have shorter relationships, so they have had less time to accumulate charges. This lifetime total should be interpreted alongside tenure, not as evidence that lower totals drive churn.

### 3. Is churn associated with payment method?

The churn rate is highest among customers using **electronic check (45.29%; 1,071 of 2,365)**. Rates are lower for mailed check (**19.11%**), automatic bank transfer (**16.71%**), and automatic credit card (**15.24%**). The electronic-check segment is a strong candidate for a billing-experience review and retention outreach. Payment method may also track with other customer differences, so the association is not causal.

### 4. Does internet service type distinguish churn risk?

Customers with **fiber optic service churn at 41.89%** (1,297 of 3,096), compared with **18.96%** for DSL and **7.40%** for customers with no internet service. The fiber segment merits a closer review of price, service quality, onboarding, and customer expectations before choosing an intervention.

### 5. Are support and security add-ons associated with retention?

Yes. Churn is lower among customers with Tech Support (**15.17%**) than those without it (**41.64%**), and lower with Online Security (**14.61%**) than without it (**41.77%**). Online Backup is associated with **21.53%** churn versus **39.93%** without it; Device Protection with **22.50%** versus **39.13%**. These patterns make service awareness and adoption worth testing as retention levers. Customers with no internet service form a separate segment and should not be compared as if they had declined internet add-ons.

### 6. Do streaming services or phone features separate churners clearly?

Streaming differences are modest: churn is **30.07% with Streaming TV vs. 33.52% without**, and **29.94% with Streaming Movies vs. 33.68% without**. PhoneService has similarly close rates (**26.71% with service vs. 24.93% without**), while MultipleLines is **28.61% with multiple lines vs. 25.04% without**. These features look less useful as standalone risk signals than payment, internet type, support, or security in this comparison.

### 7. What do other billing indicators and the service count show?

Paperless billing is associated with **33.57%** churn, compared with **16.33%** for paper bills. The six-service count has a non-monotonic pattern: churn ranges from **5.28%** among customers with all six selected services to **45.76%** among those with one. Customers with zero selected services have **21.41%** churn; this group includes all customers without internet and customers without the listed add-ons. Service count is therefore a screening summary, not a causal measure of the benefit of adding services.

## Business takeaways

- Review the billing journey for electronic-check and paperless-billing customers, then test clearer bill explanations or payment support.
- Investigate fiber customers' price-to-value perception and service experience.
- Test targeted onboarding and education for Tech Support and Online Security, measuring adoption and later churn.
- Use monthly charges and service mix to refine segments, while accounting for tenure and contract type in follow-up analysis.
- Treat all observed differences here as associations. Validate interventions with a controlled test or a model that accounts for customer tenure, contract, and overlapping service choices.

## Reproducible outputs

Run `python q1.py` from this folder to run the earlier EDA I analysis followed by Day 6 EDA II, print the verification and group summaries, and create two chart files:

- `Day6_EDA_II_Charts.png`
- `Day6_EDA_II_Service_Churn_Rates.png`
