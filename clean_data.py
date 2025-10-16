import os
import pandas as pd

RAW_PATH = "data/raw/telecom_customers.csv"
PROCESSED_PATH = "data/processed/telecom_customers_clean.csv"

# Ensure processed folder exists
os.makedirs("data/processed", exist_ok=True)

# Load CSV
try:
    df = pd.read_csv(RAW_PATH)
    print(f"✅ Loaded raw data: {df.shape[0]} rows, {df.shape[1]} columns")
except Exception as e:
    print(f"❌ ERROR loading CSV: {e}")
    exit()

# Cleaning
df.columns = df.columns.str.strip().str.replace(" ", "_")
df = df.drop_duplicates()

# Fill numeric missing values
if "TotalCharges" in df.columns:
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')
    df["TotalCharges"].fillna(df["TotalCharges"].median(), inplace=True)

# Convert Churn to 0/1
if "Churn" in df.columns:
    df["Churn"] = df["Churn"].map(lambda x: 1 if str(x).strip().lower() in ["yes","1","true"] else 0)

# Save cleaned CSV
try:
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"💾 Cleaned CSV saved at: {PROCESSED_PATH}")
except Exception as e:
    print(f"❌ ERROR saving CSV: {e}")
