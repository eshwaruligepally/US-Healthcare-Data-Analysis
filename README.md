# US Healthcare Data Analysis: Operational & Financial Excellence 🏥

## Project Overview
This project involves a comprehensive end-to-end analysis of a large-scale US Healthcare dataset containing **10,100 records**[cite: 1]. The primary objective was to leverage **Python** and **SQL** to identify cost drivers, analyze patient demographics, and build a predictive model for clinical test results[cite: 1, 2].

## 📂 Project Structure
* **`data/`**: Contains the raw 10,100-row healthcare CSV and dataset documentation[cite: 1].
* **`scripts/`**: Houses advanced preprocessing scripts (Feature Engineering) and SQL window functions[cite: 1].
* **`notebooks/`**: Comprehensive Jupyter Notebook containing Exploratory Data Analysis (EDA) and Statistical Testing.
* **`models/`**: Predictive Machine Learning logic using Random Forest[cite: 2].

---

## 🛠 Technical Implementation

### 1. Data Engineering & Preprocessing
* **Scale**: Handled over 10,000+ records to ensure data consistency for downstream analysis[cite: 1].
* **Conditional Imputation**: Managed missing billing values using grouped medians based on admission type to maintain data integrity[cite: 1].
* **Feature Engineering**: Developed a **Patient Risk Scoring** algorithm—calculating risk based on age demographics and clinical severity weights[cite: 2].

### 2. Strategic Business Insights
* **Cost Drivers**: Identified **Diabetes** as a primary financial burden, costing **28% more** than the average patient profile[cite: 2].
* **Operational Flow**: Discovered that **Elective admissions** are **39% more efficient** in resource utilization compared to Emergency stays[cite: 2].
* **Billing Equity**: Validated that average billing remains stable across top insurance payers (Aetna, Cigna, Medicare) within a 5% variance[cite: 2].

### 3. Statistical & Predictive Modeling
* **Hypothesis Testing**: Conducted **Independent T-Tests** to statistically validate billing variances across different admission types[cite: 2].
* **Machine Learning**: Implemented a **Random Forest Classifier** to predict diagnostic test results (`Normal`, `Abnormal`, `Inconclusive`) based on patient metrics[cite: 2].

---

## 🚀 Key Technologies
* **Languages**: Python (Pandas, NumPy, Scikit-learn, Scipy), SQL (PostgreSQL/MySQL)[cite: 1, 2].
* **Visualization**: Matplotlib, Seaborn, Power BI[cite: 2].
* **Methodologies**: Descriptive Statistics, Inferential Statistics, Feature Engineering, Classification Modeling[cite: 1, 2].

---
