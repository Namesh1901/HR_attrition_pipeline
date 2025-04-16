import pandas as pd
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to PostgreSQL
engine = create_engine('postgresql://postgres:postgresql@localhost:5432/hr_attrition')

# Load raw data
df_raw = pd.read_sql("SELECT * FROM int_hr_attrition_features", con=engine)

# Separate target and encode it
target = df_raw['attrition'].map({'Yes': 1, 'No': 0})

# Drop ID and target from features
df = df_raw.drop(['employeenumber', 'attrition'], axis=1)

# Encode categorical features
df = pd.get_dummies(df, drop_first=True)

# Add target column back
df['attrition'] = target

# Split into features and target
X = df.drop('attrition', axis=1)
y = df['attrition']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Plot feature importances
feature_importances = pd.Series(model.feature_importances_, index=X.columns)
plt.figure(figsize=(10, 6))
feature_importances.sort_values(ascending=False).head(10).plot(kind='barh')
plt.title("Top 10 Important Features")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Predict on all data
df['prediction'] = model.predict(X)
df['probability'] = model.predict_proba(X)[:, 1]

# Re-attach EmployeeNumber for saving
df_output = df_raw[['employeenumber']].copy()
df_output['prediction'] = df['prediction']
df_output['probability'] = df['probability']

# Save to PostgreSQL
df_output.to_sql('ml_attrition_predictions', con=engine, if_exists='replace', index=False)
