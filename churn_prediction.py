import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Define paths
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "processed", "telecom_customers_clean.csv")
RESULTS_PATH = os.path.join(BASE_DIR, "data", "results", "churn_predictions.csv")

# Create results folder if missing
os.makedirs(os.path.dirname(RESULTS_PATH), exist_ok=True)

print(f"🔍 Trying to load cleaned data from: {DATA_PATH}")
df = pd.read_csv(DATA_PATH)

# --- Identify target column automatically ---
target_col = "Churn" if "Churn" in df.columns else "Churn_Yes"

# Encode categorical variables
label_encoders = {}
for col in df.select_dtypes(include=["object"]).columns:
    if col != target_col:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

# Encode target if needed
df[target_col] = df[target_col].map({"Yes": 1, "No": 0}).fillna(df[target_col])

# Split features and target
X = df.drop(target_col, axis=1)
y = df[target_col]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model accuracy: {accuracy:.2%}")

# Save predictions
results = X_test.copy()
results["Actual_Churn"] = y_test.values
results["Predicted_Churn"] = y_pred
results.to_csv(RESULTS_PATH, index=False)

print(f"📁 Predictions saved to: {RESULTS_PATH}")
