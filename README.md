# HR_attrition_pipeline

A full-stack data analytics and machine learning pipeline built to analyze and predict employee attrition using PostgreSQL, dbt, Power BI, and Python.

---

## 🗂 Project Overview

This project simulates a real-world HR analytics scenario by:
- Cleaning and transforming raw employee data using dbt
- Generating insights and KPIs via Power BI dashboards
- Training and deploying a Random Forest classifier for attrition prediction
- Automating data refresh and ML inference workflows

---

## 🔧 Tech Stack

| Layer | Tools |
|-------|-------|
| **Database** | PostgreSQL |
| **Modeling** | dbt |
| **Dashboarding** | Power BI |
| **Machine Learning** | Python (scikit-learn, pandas) |
| **Automation** | Bash scripting / Power BI Gateway |

---

## 📊 Dashboards Preview


### 📌 Dashboard 1:
- KPI Cards: Total Attrition, Attrition Rate
- Bar Charts: Attrition by Department
- Donut Charts: Total attrition by gender
- Clustered Column Chart: Monthly income by jobrole
- Stacked Column charts: Employee Number via Agegroup and JobSatisfaction

![Attrition Overview](docs/powerbi_screenshots/Page1.png)

---

### 📌 Dashboard 2:
- Box Plot: Monthly Income by Attrition categorization
- Gauge Plot: Average predicted probability
- Scatter plot: Probability vs monthly income with Jobrole as categories
- Table : Shows top 14 employees which have highest predicted probability of attrition 

![Employee Insights](docs/powerbi_screenshots/Page2.png)

---

## 📁 Folder Structure
employee-attrition-pipeline/
│
├── 📄 README.md                  # Project documentation
├── 📂 dbt/                       # dbt project (for data modeling)
│   ├── 📄 dbt_project.yml        # dbt project config
│   ├── 📄 profiles.yml           # profile for dbt connection
│   ├── 📂 seeds/                 # Raw CSV data used in dbt
│   │   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│   └── 📂 models/                # dbt SQL models
│       ├── 📂 staging/           # Cleaned & renamed raw tables
│       │   └── stg_hr_employee_attrition.sql
│       ├── 📂 intermediate/      # Feature transformations & joins
│       │   └── int_hr_attrition_features.sql
│       ├── 📂 final/             # Fact tables / dashboards inputs
│       │   └── fct_attrition_summary.sql
│       └── 📂 ml/                # ML predictions as dbt model
│           └── ml_attrition_predictions.sql
├── 📂 ml_model/                  # Machine learning code
│   ├── ⚙️ random_forest.py     # Script to infer and write back to DB
│
├── 📂 sql_queries/               # Ad hoc and exploratory SQL
│   └── exploratory_analysis.sql
│
├── 📂 dashboards/                # Power BI files
│   └── HR_SQL_dbt_pipeline.pbix  # Power BI report file
│
├── 📂 docs/                      # Project documentation and screenshots
│   └── 📂 powerbi_screenshots/   # Screenshots for README or blog
│       ├── Page1.png
│       ├── Page2.png
│
└── 📂 scripts/                    # Optional: automation scripts (e.g. .bash)
    └── refresh_pipeline.sh

