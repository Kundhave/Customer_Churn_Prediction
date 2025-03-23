# Customer Churn Prediction API

This is a Flask API for predicting customer churn using machine learning models. The API takes customer features as input and returns the churn probability and risk level.

---

## Features
- Predicts customer churn probability.
- Returns risk level (High Risk or Low Risk).
- Deployed using Docker and Render.

---

## Usage

### API Endpoint
- **URL**: `https://customer-churn-prediction-rgwq.onrender.com/`
- **Method**: `POST`
- **Content-Type**: `text/plain``

### Request Body
Send a **comma-separated string** of feature values. For example:
```json 
1,0,0,2,1,1,1,0,1,0,0,1,1,0,1,1,100,100
```

### Example Request

```bash
curl -X POST https://your-app.onrender.com/predict \
-H "Content-Type: application/json" \
-d '{"features": [1, 0, 1, 24, 1, 0, 2, 1, 1, 0, 1, 0, 1, 1, 0, 3, 80, 1500]}'
```
### Example Response

```bash
{
    "churn_probability": "92.68%",
    "risk_level": "High Risk"
}
```
## Requirements 
-pandas

-numpy

-seaborn

-matplotlib

-Python 3.9

-Flask

-XGBoost

-Scikit-learn

-Docker (for containerization

-pickle-mixin

## Installation
1. Clone the Repository
```bash
git clone https://github.com/<your-username>/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Run the Flask App Locally
```bash
python app.py
```

-The app will be available at http://127.0.0.1:5000.




