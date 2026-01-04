# employee-attrition-analysis (Python and Tableau)

## Project Overview
This project explores factors contributing to employee attrition using a dataset from IBM HR Analytics. 

The analysis focuses on understanding *who is leaving and why*, using exploratory data analysis (EDA) in Python and preparing the data for future visualization and modeling in Tableau.

## Objectives
- Analyze overall employee attrition trends  
- Identify key demographic, job-related, and satisfaction factors linked to attrition  
- Generate actionable business insights to support HR retention strategies  
- Prepare cleaned data for Tableau dashboards and predictive modeling 

## Dataset
- **Source:** IBM HR Analytics Dataset (Kaggle)
- **Size:** 1,470 employees × 35 features
- **Target Variable:** Attrition (Yes / No)

## Tools used
- **Python:** pandas, numpy, matplotlib, seaborn  
- **Environment:** Jupyter Notebook, VS Code  
- **Visualization (Planned):** Tableau


## Methodology

### 1. Data Cleaning & Preparation
- Loaded dataset and reviewed data types and structure  
- Checked for missing values and data quality issues  
- Encoded categorical variables (e.g., Attrition → 1 = Left, 0 = Stayed)  
- Created derived features such as age groups  

### 2. Exploratory Data Analysis (EDA)
EDA was used to explore distributions, relationships, and patterns before modeling.

Key EDA techniques included:
- Attrition distribution and class imbalance analysis  
- Attrition **rates** (not just counts) across key dimensions:
  - Age groups
  - Department and Job Role
  - Job Level and Monthly Income
  - Job Satisfaction and Environment Satisfaction
  - Work-Life Balance and Overtime
- Correlation analysis using a heatmap to identify relationships between numeric variables  

### 3. Insights & Interpretation 
Insights were translated into clear business interpretations, focusing on retention risks and HR implications.


## Key Findings
- Overall attrition rate is approximately **16%**
- Higher attrition observed among:
  - Younger employees (early-career stages)
  - Employees with lower job levels and income
  - Employees working overtime
- Lower job satisfaction, environment satisfaction, and work-life balance are associated with higher attrition
- Attrition patterns vary significantly by department and job role

## Business Implications
- Early-career employees and lower-level roles may require targeted retention strategies  
- Managing overtime and improving work-life balance could reduce turnover risk  
- Satisfaction metrics provide valuable early signals for employee disengagement  

## Limitations
- Dataset is synthetic and cross-sectional (no time-series tracking)  
- Correlation does not imply causation  
- Attrition class imbalance (majority stayers) may affect predictive modeling  

## Next Steps
- Conduct statistical tests to compare attrition vs non-attrition groups  
- Build predictive models (e.g., logistic regression) to identify high-risk employees  
- Export cleaned data to Tableau for interactive dashboards  
- Apply feature engineering to improve modeling performance  


## Project Status
This project is an ongoing learning project focused on developing practical data analysis and visualization skills.
