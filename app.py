import gradio as gr
import pandas as pd
import pickle

# Load model
model = pickle.load(open("churn_model.pkl", "rb"))

def predict_churn(tenure, monthly, total, contract, payment):

    contract_map = {
        "Month-to-month": 0,
        "One year": 1,
        "Two year": 2
    }

    payment_map = {
        "Electronic check": 0,
        "Mailed check": 1,
        "Bank transfer": 2,
        "Credit card": 3
    }

    input_data = pd.DataFrame([[tenure, monthly, total,
                                contract_map[contract],
                                payment_map[payment]]],
                              columns=['tenure','MonthlyCharges','TotalCharges','Contract','PaymentMethod'])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)

    if prediction[0] == 1:
        return f"❌ Customer likely to CHURN\nConfidence: {round(probability[0][1]*100,2)}%"
    else:
        return f"✅ Customer likely to STAY\nConfidence: {round(probability[0][0]*100,2)}%"


interface = gr.Interface(
    fn=predict_churn,
    inputs=[
        gr.Slider(0, 72, label="Tenure (months)"),
        gr.Number(label="Monthly Charges"),
        gr.Number(label="Total Charges"),
        gr.Dropdown(["Month-to-month", "One year", "Two year"], label="Contract Type"),
        gr.Dropdown(["Electronic check", "Mailed check", "Bank transfer", "Credit card"], label="Payment Method")
    ],
    outputs="text",
    title="📊 Customer Churn Prediction System",
    description="Enter customer details to predict churn"
)

interface.launch()