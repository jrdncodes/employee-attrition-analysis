import pandas as pd

df = pd.read_csv("employee_attrition_ibm_hr.csv")

#print(df.head(20))
#print(df.info())
print(df.columns)
#print(df.describe())

# Check for missing values
#print(df.isnull().sum()) 

# Basic statistical analysis
print("Average Age:", df['Age'].mean())
print("Median Monthly Income:", df['MonthlyIncome'].median())
print("Years at company:", df['YearsAtCompany'].std())
