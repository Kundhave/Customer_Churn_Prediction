# Customer Churn Prediction API

This is a Flask API for predicting customer churn using machine learning models. The API takes customer features as input and returns the churn probability and risk level.
---

## Features
- Predicts customer churn probability (Drop-off probability)
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

### Overview:

![image](https://github.com/user-attachments/assets/e6404cbf-c7b0-42cf-a507-4ff8ee39430e)


![image](https://github.com/user-attachments/assets/34040d6e-8014-4ce5-b8d6-6620b69cb141)


![image](https://github.com/user-attachments/assets/aa7aebf1-e0da-4103-8e93-bc2eeb7b9513)


![image](https://github.com/user-attachments/assets/4015891b-0276-489b-a4bc-9706e8290c85)


![image](https://github.com/user-attachments/assets/ae58269c-524c-4367-b22a-1fcb2ff345e4)


![image](https://github.com/user-attachments/assets/60737f58-6fd9-4059-aac9-ba4be5608a73)


## Requirements 
- pandas

- numpy

- seaborn

- matplotlib

- Python 3.9

- Flask

- XGBoost

- Scikit-learn

- Docker (for containerization

- pickle-mixin

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

- The app will be available at http://127.0.0.1:5000.

---
### Deployment
1. Build the Docker Image
```bash
docker build -t churn-prediction-api
```

2. Run the Docker Container
```bash
docker run -p 5000:5000 churn-prediction-api
```

3. Deploy to Render
- Push the Docker image to Docker Hub.
- Connect your Docker Hub repository to Render.

- Set the port to 5000 and deploy.

## Project Structure
```
Customer_Churn_Prediction/
├── app.py                  # Flask API code
├── best_xgb_model.pkl      # Trained XGBoost model
├── scaler.pkl              # Scaler for preprocessing
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
└── README.md               # Project documentation
```

## Contributing
- Contributions are welcome! If you find any issues or want to enhance the project, feel free to open a pull request.



