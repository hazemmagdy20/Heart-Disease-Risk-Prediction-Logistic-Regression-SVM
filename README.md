# Heart-Disease-Risk-Prediction-Logistic-Regression-SVM
This project aims to predict the 10-year risk of heart disease using patient health data.

## 📌 Project Overview

This project aims to predict the 10-year risk of heart disease using patient health data.
Multiple machine learning models were trained and evaluated, starting with Logistic Regression, then improving with SVM.
The goal is to assist in early medical risk detection by identifying individuals with higher chances of developing heart disease.
This project walks through Data Cleaning → Preprocessing → Handling Imbalance → Model Training → Threshold Optimization → Evaluation → Model Selection for Deployment.

---

## 📂 Dataset Description

| Column Name   | Description |
|--------------|------------|
| Sex      | 1 = Male, 0 = Female |
| age       | Patient age in years |
| currentSmoker          | 1 if smokes currently, else 0 |
| cigsPerDay       | Number of cigarettes smoked per day |
| BPMeds       | On blood pressure medication (1/0) |
| prevalentStroke     | History of stroke (1/0) |
| prevalentHyp   | Hypertension diagnosed (1/0) |
| diabetes    | Diabetes diagnosis (1/0) |
| totChol     | Calories burnt during the workout |
| sysBP     | Systolic blood pressure |
| diaBP   | Diastolic blood pressure |
| BMI    | Body mass index |
| heartRate     | Resting heart rate |
| glucose     | Blood glucose level |
| TenYearCHD (Target)    | 1 = Risk of heart disease in 10 years, 0 = No risk |

---

## 🧹 Data Preprocessing Steps

- Loaded and inspected the dataset (shape: 4240 × 16):
  ```python
  - head()
  - tail()
  - Shape (shape: 4240 × 16)
- Renamed male → Sex for clarity:
  ```python
  - rename()
- Removed education due to low impact on correlation and missing rate:
  ```python
  - drop()
- Handled missing values (imputed some fields + dropped excessive missing rows):
  ```python
  - isnull().sum()
  - Apply imputation
  - Apply dropana()
- Apply EDA (Exploratory Data Analysis):
  ```python
  - info()
  - describe() 
  - corr()
- Standardized numerical features using StandardScaler:
  ```python
  - StandarSacaler()
- Handled class imbalance using SMOTE transforming data from:
  ```python
  - Before SMOTE: 0 → 3506 , 1 → 614
  - After SMOTE:  0 → 3506 , 1 → 3506
- Split data: 80% train / 20% test:
  ```python
  - train_test_split()

---

## 🤖 Models Trained & Results

## 1️⃣ Logistic Regression (Baseline - threshold 0.50)  
- Results: 
  ```python
  - Accuracy : 0.67
  - Recall (CHD=1) : 0.66
  - Precision : 0.68
- 🟡 Good starting point but missed many positive cases (medical risk) 

## 2️⃣ Logistic Regression (Optimized Thresholds)
- We applyed balanced class weight & lowered the decision threshold to increase Recall (detect more risky patients):
- Results:
  | Threshold | Recall↑                 | Precision↓ | Accuracy |
  | --------- | ----------------------- | ---------- | -------- |
  | 0.50      | 0.66                    | 0.68       | 0.67     |
  | **0.45**  | **0.75**                | 0.66       | **0.68** |
  | 0.40      | **0.80 (best medical)** | 0.64       | 0.67     |
  
- In healthcare, Recall matters more to avoid missing at-risk patients.

## 3️⃣ Support Vector Machine (SVM) – Final Model
- Results:
  ```python
  Accuracy : 0.73
  Precision : 0.73
  Recall    : 0.74
  F1 Score  : 0.73
- Best performing model overall
- Balanced recall & precision
- Will be Used for deployment

---

## 🏁 Final Decision

| Model               | Role                                                 |
| ------------------- | ---------------------------------------------------- |
| **SVM**             | 🚀 Selected for Deployment (best performance)        |
| Logistic Regression | 📊 Kept for interpretability and medical explanation |

- In real-world medical prediction:
  ```python
  - Logistic Regression = Explain why the model predicted risk
  - SVM = Best for actual predictive performance

---

## Model Deployment
- Steps for deployment:
   ```python
   - Models & Scaler Saved using joblib.
   - Deployment Done using Flask.
   - Built Interactive UI.
   - The Patients enter the inputs and then get predection based on their inputs.
- Screenshot:
  <img width="1043" height="720" alt="image" src="https://github.com/user-attachments/assets/b535acaa-58d7-4020-a405-a393405e753e" />
  <img width="1020" height="709" alt="image" src="https://github.com/user-attachments/assets/95331481-429b-4b35-b9cb-c84582a87e2d" />
  <img width="1016" height="178" alt="image" src="https://github.com/user-attachments/assets/67e205db-0331-40f0-aa58-93dfc988ccc4" />


