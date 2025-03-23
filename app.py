from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

xgb_model = pickle.load(open("xgb_model.pkl", "rb"))
rf_model = pickle.load(open("rf_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html") 

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        features = np.array(data["features"]).reshape(1, -1)
        model_choice = data.get("model", "xgb") 

        features_scaled = scaler.transform(features)
        model = rf_model if model_choice == "rf" else xgb_model

        prediction = model.predict(features_scaled)[0]  
        probability = model.predict_proba(features_scaled)[0][1]  

        risk_level = "Low Risk" if prediction == 0 else "High Risk"
        probability_percent = round(probability * 100, 2) 

        
        response = {
            "selected_model": model_choice,
            "risk_level": risk_level,  
            "churn_probability": f"{probability_percent}%"
        }

        return jsonify(response)
    
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
