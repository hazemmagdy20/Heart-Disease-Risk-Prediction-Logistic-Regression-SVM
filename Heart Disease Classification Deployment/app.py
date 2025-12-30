from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model & scaler
model = joblib.load("SVC_model.pkl")
scaler = joblib.load("Scaler_HDC.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values
        data = [
            float(request.form['Sex']),           # 0/1
            float(request.form['age']),
            float(request.form['currentSmoker']), # 0/1
            float(request.form['cigsPerDay']),
            float(request.form['BPMeds']),        # 0/1
            float(request.form['prevalentStroke']),#0/1
            float(request.form['prevalentHyp']),  # 0/1
            float(request.form['diabetes']),      # 0/1
            float(request.form['totChol']),
            float(request.form['sysBP']),
            float(request.form['diaBP']),
            float(request.form['BMI']),
            float(request.form['heartRate']),
            float(request.form['glucose'])
        ]

        scaled_data = scaler.transform([data])
        prediction = model.predict(scaled_data)[0]

        result = "⚠️ High Risk: May develop heart disease in 10 years" if prediction == 1 else "✔️ Safe: No predicted risk in 10 years"

        return render_template('index.html', prediction_text=result)

    except:
        return render_template('index.html', prediction_text="❌ Error! Please check your inputs.")

if __name__ == "__main__":
    app.run(debug=True)

