# Customer Churn Analysis

## Day 2 — Data Understanding

### Step 9 — Important Columns

**Why?**
We want to connect the columns in the dataset to the project's business questions.
(نريد ربط الأعمدة الموجودة في البيانات بأسئلة المشروع.)

We are not trying to identify the most important factor or prove any relationship at this stage.
(نحن لا نحاول تحديد أهم عامل أو إثبات وجود علاقة في هذه المرحلة.)

We are only identifying variables that may be useful for the analysis later.
(نحن فقط نحدد المتغيرات التي قد تكون مفيدة للتحليل لاحقًا.)

### Important Variables

```text
gender → May help compare churn rates between customers by gender.
(قد يساعد في مقارنة معدلات مغادرة العملاء حسب الجنس.)

SeniorCitizen → May help examine differences in churn between older customers and other customers.
(قد يساعد في دراسة الاختلاف في مغادرة العملاء بين كبار السن وبقية العملاء.)

tenure → Directly related to the question of whether customer tenure may be associated with churn.
(مرتبط مباشرة بسؤال ما إذا كانت مدة بقاء العميل قد تكون مرتبطة بمغادرة العميل.)

Contract → Related to the question of whether contract type may be associated with churn.
(مرتبط بسؤال ما إذا كان نوع العقد قد يكون مرتبطًا بمغادرة العميل.)

PaymentMethod → May help analyze whether payment method is associated with differences in churn.
(قد يساعد في تحليل ما إذا كانت طريقة الدفع مرتبطة باختلاف معدلات المغادرة.)

MonthlyCharges → Directly related to the question of whether monthly charges may be associated with churn.
(مرتبط مباشرة بسؤال ما إذا كانت الرسوم الشهرية قد تكون مرتبطة بمغادرة العميل.)

InternetService → May help analyze differences in churn across internet service types.
(قد يساعد في تحليل الاختلافات في مغادرة العملاء حسب نوع خدمة الإنترنت.)

TechSupport → May help examine whether technical support availability is associated with churn.
(قد يساعد في دراسة ما إذا كان توفر الدعم الفني مرتبطًا بمغادرة العميل.)

Churn → The target variable that indicates whether a customer left the company or not.
(المتغير المستهدف الذي يوضح ما إذا كان العميل غادر الشركة أم لا.)
```

---

# Step 10 — Data Understanding Notes

### Dataset Size

The dataset contains **7,043 rows and 21 columns**.
(تحتوي البيانات على 7,043 صف و21 عمودًا.)

### Structure

Each row represents a customer, and each column represents a customer attribute or service-related variable.
(كل صف يمثل عميلًا، وكل عمود يمثل خاصية للعميل أو متغيرًا متعلقًا بالخدمة.)

### Data Types

The dataset contains numerical and categorical variables.
(تحتوي البيانات على متغيرات رقمية ومتغيرات فئوية.)

Some columns may require data type conversion before analysis.
(قد تحتاج بعض الأعمدة إلى تحويل نوع البيانات قبل التحليل.)

### Missing Values

There are missing values in some columns, especially **TotalCharges**.
(توجد قيم مفقودة في بعض الأعمدة، وخصوصًا TotalCharges.)

These missing values should be investigated and handled during the data-cleaning stage.
(يجب فحص هذه القيم المفقودة ومعالجتها خلال مرحلة تنظيف البيانات.)

### Duplicates

The dataset should be checked for duplicate records before analysis.
(يجب فحص البيانات للتأكد من عدم وجود سجلات مكررة قبل التحليل.)

### Churn Distribution

The **Churn** column contains two categories: **Yes** and **No**.
(يحتوي عمود Churn على فئتين: Yes و No.)

The distribution of these categories should be examined to understand whether the target variable is balanced or imbalanced.
(يجب فحص توزيع هذه الفئات لمعرفة ما إذا كان المتغير المستهدف متوازنًا أم غير متوازن.)

### Potential Data-Quality Issues

Potential issues include missing values, inconsistent data types, categorical values, and possible formatting problems.
(تشمل مشكلات جودة البيانات المحتملة القيم المفقودة، وأنواع البيانات غير المناسبة، والقيم الفئوية، ومشكلات التنسيق المحتملة.)

These issues will be investigated and handled during Day 3 — Data Cleaning.
(سيتم فحص هذه المشكلات ومعالجتها خلال اليوم الثالث — تنظيف البيانات.)

### Important Variables

The variables identified as potentially useful for the analysis include:

* **gender** (الجنس)
* **SeniorCitizen** (كبير السن)
* **tenure** (مدة بقاء العميل)
* **Contract** (نوع العقد)
* **PaymentMethod** (طريقة الدفع)
* **MonthlyCharges** (الرسوم الشهرية)
* **InternetService** (خدمة الإنترنت)
* **TechSupport** (الدعم الفني)
* **Churn** (مغادرة العميل)

---

# Day 3 — Data Cleaning

## Goal

The goal of Day 3 is to identify and handle data-quality problems before starting deeper analysis.
(هدف اليوم الثالث هو اكتشاف ومعالجة مشكلات جودة البيانات قبل البدء في التحليل المتقدم.)

We will focus on missing values, duplicates, data types, inconsistent values, and other potential quality issues.
(سنركز على القيم المفقودة، والتكرارات، وأنواع البيانات، والقيم غير المتسقة، وأي مشكلات أخرى في جودة البيانات.)

---

## Step 1 — Create a Clean Working Copy

### Why?

We keep the original dataset unchanged and perform cleaning on a separate copy.
(نحافظ على البيانات الأصلية بدون تغيير وننفذ التنظيف على نسخة منفصلة.)

### Task

Create a copy of the original DataFrame and use the copy for all cleaning operations.

---

## Step 2 — Check Missing Values

### Why?

Missing values can affect calculations and analysis.
(القيم المفقودة قد تؤثر على الحسابات والتحليل.)

### Task

Check the number of missing values in every column.

Focus especially on:

```text
TotalCharges
```

Record:

* Which columns contain missing values?
* How many missing values does each column contain?

---

## Step 3 — Investigate Missing Values

### Why?

We should understand why the values are missing before deciding how to handle them.
(يجب أن نفهم سبب وجود القيم المفقودة قبل اتخاذ قرار بشأن طريقة معالجتها.)

### Task

Investigate the rows where **TotalCharges** is missing.

Check whether these customers have:

```text
tenure = 0
```

Then think about whether the missing values represent a data-entry issue or a meaningful situation.

---

## Step 4 — Handle Missing Values

### Why?

After understanding the missing values, we can choose an appropriate cleaning method.
(بعد فهم القيم المفقودة، يمكننا اختيار الطريقة المناسبة لمعالجتها.)

### Task

Decide how to handle the missing **TotalCharges** values.

Before applying the decision, write a short note explaining:

```text
What I found:
Why I chose this method:
```

---

## Step 5 — Check Duplicate Rows

### Why?

Duplicate records can affect counts and analysis results.
(السجلات المكررة قد تؤثر على الأعداد ونتائج التحليل.)

### Task

Check whether the dataset contains duplicate rows.

Record:

```text
Number of duplicate rows:
```

If duplicates exist, determine whether they are exact duplicates before removing anything.

---

## Step 6 — Check Data Types

### Why?

Correct data types are important for calculations and analysis.
(أنواع البيانات الصحيحة مهمة للحسابات والتحليل.)

### Task

Review the data types of all columns.

Pay special attention to:

```text
TotalCharges
SeniorCitizen
Churn
```

Identify any column whose data type may not be appropriate for analysis.

---

## Step 7 — Convert Incorrect Data Types

### Why?

Some columns may be stored in an inappropriate format, which can prevent correct calculations.
(قد تكون بعض الأعمدة مخزنة بصيغة غير مناسبة، مما قد يمنع إجراء الحسابات بشكل صحيح.)

### Task

Convert any incorrectly stored numerical column into an appropriate numerical data type.

After conversion, verify the result.

---

## Step 8 — Check Categorical Values

### Why?

Categorical columns should contain consistent and expected values.
(يجب أن تحتوي الأعمدة الفئوية على قيم متناسقة ومتوقعة.)

### Task

Check the unique values of important categorical columns such as:

```text
gender
Contract
PaymentMethod
InternetService
TechSupport
Churn
```

Look for:

* Unexpected values
* Spelling differences
* Extra spaces
* Inconsistent categories

Do not modify a value unless there is evidence that it is incorrect.

---

## Step 9 — Check Numerical Values

### Why?

Numerical columns should contain reasonable values and should not contain unexpected negative or impossible values.
(يجب أن تحتوي الأعمدة الرقمية على قيم منطقية وألا تحتوي على قيم سالبة أو غير ممكنة بشكل غير متوقع.)

### Task

Review important numerical columns such as:

```text
tenure
MonthlyCharges
TotalCharges
```

Check their:

* Minimum
* Maximum
* Mean

Look for values that require further investigation.

---

## Step 10 — Final Data-Quality Check

### Why?

We need to confirm that the cleaning process did not create new problems.
(نحتاج إلى التأكد من أن عملية التنظيف لم تسبب مشكلات جديدة.)

### Task

Run a final check for:

```text
Missing values
Duplicates
Data types
Categorical consistency
Numerical values
```

Record the final dataset shape:

```text
Rows:
Columns:
```

---

## Day 3 — Documentation

At the end of Day 3, write a short summary containing:

```text
1. Missing values found:
2. How missing values were handled:
3. Duplicate rows found:
4. Data types changed:
5. Categorical issues found:
6. Numerical issues found:
7. Final dataset size:
8. Final data-quality status:
```

### Important Rule

Do not start Data Visualization or deeper analysis during Day 3.

The purpose of Day 3 is to make the dataset clean and ready for analysis.
(هدف اليوم الثالث هو تجهيز البيانات وتنظيفها لتصبح جاهزة للتحليل.)
