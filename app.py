from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load models & scaler
xgb_model = pickle.load(open("xgb_model.pkl", "rb"))
rf_model = pickle.load(open("rf_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # Load frontend

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data from the request
        data = request.json
        features = np.array(data["features"]).reshape(1, -1)
        model_choice = data.get("model", "xgb")  # Default to XGBoost

        # Scale input
        features_scaled = scaler.transform(features)

        # Select model
        model = rf_model if model_choice == "rf" else xgb_model

        # Predict churn
        prediction = model.predict(features_scaled)[0]  # 0 or 1
        probability = model.predict_proba(features_scaled)[0][1]  # Probability of churn (class 1)

        # Determine risk level
        risk_level = "Low Risk" if prediction == 0 else "High Risk"
        probability_percent = round(probability * 100, 2)  # Convert to percentage

        # Prepare response
        response = {
            "selected_model": model_choice,
            "risk_level": risk_level,  # Only include descriptive risk level
            "churn_probability": f"{probability_percent}%"
        }

        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
