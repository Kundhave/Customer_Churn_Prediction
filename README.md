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

- **URL**: `https://your-app.onrender.com/predict`
- **Method**: `POST`
- **Content-Type**: `application/json`

### Request Body

Send a JSON payload with the following structure:

```json
{
    "features": [1, 0, 0, 2, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 100, 100]
}
Example Request
bash
Copy
curl -X POST https://your-app.onrender.com/predict \
     -H "Content-Type: application/json" \
     -d '{"features": [1, 0, 0, 2, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 100, 100]}'
Example Response
json
Copy
{
    "churn_probability": "92.68%",
    "risk_level": "High Risk"
}
Requirements
Python 3.9

Flask

XGBoost

Scikit-learn

Docker (for containerization)

Installation
1. Clone the Repository
bash
Copy
git clone https://github.com/<your-username>/Customer_Churn_Prediction.git
cd Customer_Churn_Prediction
2. Install Dependencies
bash
Copy
pip install -r requirements.txt
3. Run the Flask App Locally
bash
Copy
python app.py
The app will be available at http://127.0.0.1:5000.

Deployment
1. Build the Docker Image
bash
Copy
docker build -t churn-prediction-api .
2. Run the Docker Container
bash
Copy
docker run -p 5000:5000 churn-prediction-api
3. Deploy to Render
Push the Docker Image to Docker Hub:

Tag and push your Docker image to Docker Hub:

bash
Copy
docker tag churn-prediction-api <your-dockerhub-username>/churn-prediction-api:latest
docker push <your-dockerhub-username>/churn-prediction-api:latest
Connect Your Docker Hub Repository to Render:

Go to Render.

Create a new Web Service and connect your Docker Hub repository.

Set the Port to 5000:

In the Render dashboard, set the Port to 5000.

Deploy:

Click Create Web Service to deploy your app.

Project Structure
Copy
Customer_Churn_Prediction/
├── app.py                  # Flask API code
├── best_xgb_model.pkl      # Trained XGBoost model
├── scaler.pkl              # Scaler for preprocessing
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
└── README.md               # Project documentation
Contributing
Contributions are welcome! If you find any issues or want to enhance the project, feel free to open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For questions or feedback, please contact:

Your Name: Your Email

GitHub: Your GitHub Profile

Copy

---

### **Key Fixes in the README.md**
1. **Headers (Hashes)**:
   - Used `#`, `##`, and `###` for headings and subheadings.
   - Example:
     ```markdown
     ## Usage
     ### API Endpoint
     ```

2. **Lists**:
   - Used `-` for unordered lists.
   - Example:
     ```markdown
     - Predicts customer churn probability.
     - Returns risk level (High Risk or Low Risk).
     ```

3. **Code Blocks**:
   - Used triple backticks (```) for code blocks.
   - Example:
     ```markdown
     ```bash
     docker build -t churn-prediction-api .
     ```
     ```

4. **Bold and Italics**:
   - Used `**` for bold and `*` for italics.
   - Example:
     ```markdown
     **URL**: `https://your-app.onrender.com/predict`
     ```

5. **Proper Indentation**:
   - Ensured proper indentation for nested lists and code blocks.

---

### **How to Add This to Your GitHub Repository**
1. **Create a `README.md` File**:
   - In your project directory, create a new file named `README.md`.

2. **Copy and Paste the Content**:
   - Copy the above content and paste it into the `README.md` file.

3. **Push to GitHub**:
   - Add, commit, and push the `README.md` file to your GitHub repository:
     ```bash
     git add README.md
     git commit -m "Add README.md"
     git push origin main
     ```

4. **View on GitHub**:
   - Go to your GitHub repository page. The `README.md` file will be displayed at the bottom of the page.

---

This properly formatted `README.md` will display correctly on GitHub and provide a clear overview of your project. Let me know if you need further assistance! 😊
