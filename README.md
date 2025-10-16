# Customer Churn Analysis

### 📊 Overview
This project analyzes telecom customer data to identify customers at risk of churn. It uses **Python (Pandas, Scikit-learn)** for data preprocessing and predictive modeling, and **Power BI** for visualization and dashboard creation. The goal is to help the business focus on high-risk segments and improve customer retention strategies.

---

### 🛠 Tools Used
- **Python**: Pandas, Scikit-learn
- **Power BI**: Dashboard and visualization
- **CSV files**: Input and output data

---

### 🧱 Project Structure

customer_churn_analysis/
│
├── data/
│   ├── raw/
│   │   └── telecom_customers.csv         # Original raw dataset
│   └── processed/
│       └── telecom_customers_clean.csv   # Cleaned dataset
│
├── scripts/
│   ├── clean_data.py                      # Data cleaning script
│   └── churn_prediction.py                # Prediction/ML script
│
├── results/
│   └── churn_predictions.csv              # Predicted churn output
│
├── PowerBI/
│   └── Customer_Churn_Dashboard.pbix     # Power BI dashboard file
│
├── README.md                              # Project description
└── requirements.txt                       # Python dependencies

---

### 📝 Steps to Run the Project

1. **Install Dependencies**  
   Make sure you have Python installed. Install required packages:
   ```bash
   pip install -r requirements.txt

2. **Data Cleaning
   python3 scripts/clean_data.py
3. Churn Prediction
   Run the prediction script:

   python3 scripts/churn_prediction.py
4. PowerBI Dashboard
  - Open PowerBI/Customer_Churn_Dashboard.pbix

  - Load results/churn_predictions.csv

  - Explore churn insights using charts
    
🔍 Suggested Graphs in Power BI

  Overall Churn Distribution

  Predicted vs Actual Churn

  Churn by Gender

  Churn by Contract Type
  
✅ Cross-Check

You can cross-check the results using Python:

import pandas as pd

# Load predictions
df = pd.read_csv("results/churn_predictions.csv")

# Check churn counts
print(df['Actual_Churn'].value_counts())

# Check churn by gender
print(df.groupby('gender')['Actual_Churn'].value_counts())

📁 Output

results/churn_predictions.csv – Predicted churn dataset

PowerBI/Customer_Churn_Dashboard.pbix – Dashboard visualization
