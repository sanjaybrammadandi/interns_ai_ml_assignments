📊 Customer Churn Data Cleaning (ML-Ready) 📌 Project Overview

This project demonstrates a practical data cleaning workflow for a messy Customer Churn dataset. The dataset contains common real-world data quality issues that must be resolved before training machine learning models.

The goal is to transform raw, inconsistent data into a clean, numeric, ML-ready dataset using Python, pandas, and scikit-learn.

🧪 Problems in the Raw Dataset

The original dataset intentionally includes the following issues:

❌ Missing values in the Age column

❌ Duplicate records

❌ Inconsistent categorical values in Gender

(M, male, Female, FEMALE, etc.)

❌ Extreme Salary outliers

❌ Mixed data formats not suitable for ML models

🛠️ Cleaning Strategy (ML-Oriented)

The cleaning process follows best practices commonly used in industry ML pipelines:

Remove duplicate rows

Standardize categorical values (Gender)

Impute missing values (Age)

Detect and treat outliers (Salary)

Encode categorical variables

Scale numerical features

Export a clean dataset ready for ML models

📂 Project Structure customer-churn-cleaning/ │ ├── customer_churn_messy.csv # Raw messy dataset ├── clean_customer_churn.py # Data cleaning script ├── customer_churn_cleaned.csv # Output (generated) └── README.md # Project documentation

▶️ How to Run the Project 1️⃣ Install Dependencies

Make sure Python is installed, then run:

pip install pandas numpy scikit-learn

2️⃣ Run the Cleaning Script python clean_customer_churn.py

3️⃣ Output

After execution:

Cleaned data is saved as customer_churn_cleaned.csv

Console displays before & after snapshots

Dataset is fully numeric and ML-ready

🧩 Code Explanation (Step-by-Step)

Load & Inspect Data df = pd.read_csv("customer_churn.csv") df.info() df.head()
✔ Understand structure, missing values, and data types

Remove Duplicate Rows df = df.drop_duplicates()
✔ Prevents biased model learning and data leakage

Standardize Gender Values df['Gender'] = ( df['Gender'] .str.strip() .str.lower() .replace({'m': 'male', 'f': 'female'}) )
✔ Ensures consistent categorical values

Handle Missing Age Values df['Age'] = df['Age'].fillna(df['Age'].median())
✔ Median imputation is robust to outliers

Detect & Treat Salary Outliers (IQR Method) Q1 = df['Salary'].quantile(0.25) Q3 = df['Salary'].quantile(0.75) IQR = Q3 - Q1
Outlier treatment (capping):

df['Salary'] = np.clip(df['Salary'], lower_bound, upper_bound)

✔ Preserves data while reducing distortion

Encode Categorical Variables df = pd.get_dummies(df, columns=['Gender'], drop_first=True)
✔ Converts text into numeric features for ML

Scale Numerical Features scaler = StandardScaler() df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])
✔ Ensures features are on the same scale for models like:

Logistic Regression

SVM

Neural Networks

✅ Final Dataset Characteristics

✔ No missing values

✔ No duplicate rows

✔ All numeric features

✔ Scaled and encoded

✔ Ready for ML training

Final columns example:

CustomerID | Age | Salary | Churn | Gender_male

🧠 Interview-Ready Summary

“I cleaned the dataset by removing duplicates, standardizing categorical values, imputing missing ages using the median, treating salary outliers with IQR capping, encoding categorical features, and scaling numerical variables to prepare the data for machine learning.”

🚀 Possible Extensions

Convert to a scikit-learn Pipeline

Add EDA visualizations

Train Logistic Regression / XGBoost

Perform feature engineering

Add train-test split & evaluation