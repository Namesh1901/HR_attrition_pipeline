import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:postgresql@localhost:5432/hr_attrition')

# Load data from the feature table
df_raw = pd.read_sql("SELECT * FROM int_hr_attrition_features", con=engine)

# Keep a copy of the employee number for final output
employee_ids = df_raw[['employeenumber']].copy()
print(df_raw.columns)
