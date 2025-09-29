import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("employee_attrition_ibm_hr.csv")

# Initial data exploration
#print(df.head(20))
#print(df.info())
#print(df.columns)
#print(df.describe())

# Check for missing values
#print(df.isnull().sum()) 


education_map = {1: 'Below College', 2: 'College', 3: 'Bachelor', 4: 'Master', 5: 'Doctor'}
job_satisfaction_map = {1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High'}
worklife_map = {1: 'Bad', 2: 'Good', 3: 'Better', 4: 'Best'}

df['Education'] = df['Education'].map(education_map)
df['JobSatisfaction'] = df['JobSatisfaction'].map(job_satisfaction_map)
df['WorkLifeBalance'] = df['WorkLifeBalance'].map(worklife_map)

# Basic statistical analysis
print("Average Age: {:.2f}".format(df['Age'].mean()))
print("Median Monthly Income:", df['MonthlyIncome'].median())
print("Years at company:", df['YearsAtCompany'].std())

# Attrition counts
attrition_counts = df['Attrition'].value_counts()
print("\nAttrition counts:\n", attrition_counts)