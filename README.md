# 📊 Customer Churn Prediction System

## 👤 Student Details

* **Name:** Prasannata Shashikant Raut
* **Roll No:** AIML-A6/FEB-9012
* **Course:** AIML

---

## 🚀 Overview

This project is an end-to-end Machine Learning application that predicts whether a customer is likely to churn based on their service usage and billing details. It includes data preprocessing, model training, evaluation, and an interactive web interface using Gradio.

---

## 🎯 Objective

To build a predictive system that helps businesses identify customers at risk of leaving, allowing them to take proactive retention measures.

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Gradio (UI)

---

## 📁 Project Structure

```
├── app.py              # Gradio UI
├── train.py            # Model training script
├── churn.csv           # Dataset
├── requirements.txt    # Dependencies
└── churn_model.pkl     # Trained model (generated)
```

---

## ⚙️ Workflow

1. Load dataset
2. Data cleaning and preprocessing
3. Feature selection and encoding
4. Model training (Random Forest)
5. Model evaluation
6. Save trained model
7. Predict churn using UI

---

## 📊 Model Details

* Algorithm: Random Forest Classifier
* Accuracy: ~75% – 85%
* Metrics:

  * Accuracy Score
  * Confusion Matrix
  * Classification Report

---

## 🎨 User Interface

The project includes an interactive UI built with Gradio where users can:

* Enter customer details
* Get real-time churn prediction
* View prediction confidence

---

## ▶️ How to Run

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Train model

```
python train.py
```

### 3. Run application

```
python app.py
```

---

## 🧪 Sample Test Inputs

### ❌ Likely to Churn

* Tenure: 5
* Monthly Charges: 100
* Total Charges: 500
* Contract: Month-to-month
* Payment: Electronic check

### ✅ Likely to Stay

* Tenure: 60
* Monthly Charges: 40
* Total Charges: 2400
* Contract: Two year
* Payment: Credit card

---

## 📌 Key Insights

* Low tenure customers are more likely to churn
* High monthly charges increase churn probability
* Long-term contracts reduce churn

---

## 🔮 Future Scope

* Deploy application on cloud
* Add explainable AI (SHAP)
* Improve model accuracy
* Integrate real-time data

---

## ⭐ Conclusion

This project demonstrates a complete Machine Learning pipeline along with a user-friendly interface, making it a practical solution for real-world customer retention problems.
