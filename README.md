#   E-commerce Revenue Prediction Web App

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/ML-Linear_Regression-orange?style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

A web-based application that predicts e-commerce revenue in real-time. The project utilizes a **Linear Regression** model served via a **Flask API** and a clean, responsive interface for user interaction.

---

##   User Interface Overview
The frontend is designed to be simple and user-friendly, allowing users to input transaction details and receive instant predictions.
*   **Input Fields:** Quantity, Unit Price, Discount, and Category Code.
*   **Technology:** Pure HTML5, CSS3 (with Flexbox), and Vanilla JavaScript (Fetch API).
*   **Responsiveness:** Mobile-friendly design with media queries.

---

##   How it Works
1.  **User Input:** The user enters features like `Quantity` and `Unit Price` in the HTML form.
2.  **API Request:** JavaScript's `fetch()` function captures the data and sends a **POST** request to the Flask server (`/predict`) in JSON format.
3.  **Model Inference:** The Backend (Flask) loads the trained `ecommerce_model.pkl` and performs the prediction.
4.  **Display:** The predicted revenue is sent back to the browser and displayed dynamically without refreshing the page.

---

##   Project Structure
*   **`index.html`**: The main interface containing the prediction form and the `predict()` JavaScript function.
*   **`app.py`**: The Flask server that handles the `/predict` route and communicates with the ML model.
*   **`ecommerce_model.pkl`**: The serialized Linear Regression model trained on e-commerce historical data.
*   **`regression.ipynb`**: The data science notebook where the data was analyzed and the model was built.

---

##   Setup & Installation

### 1. Backend Setup
Ensure you have Python installed, then install the dependencies:
```bash
pip install flask flask-cors pandas scikit-learn
