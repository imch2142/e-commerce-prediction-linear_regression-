#   E-Commerce Customer Spending Prediction

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

An end-to-end Machine Learning project that uses **Linear Regression** to predict the annual amount spent by customers on an e-commerce platform based on their behavior and membership duration.

---

##   Project Overview
This project focuses on analyzing customer data to help an e-commerce company decide whether to focus their efforts on their mobile app or website. By leveraging **Mathematical Optimization** and **Linear Regression**, we identify the key factors that drive customer loyalty and spending.

###   File Structure Breakdown
*   **`regression.ipynb`**: Detailed Jupyter Notebook covering Data Analysis (EDA), visualization, and model training.
*   **`ecommerce_model.pkl`**: The trained and serialized Linear Regression model, ready for production use.
*   **`app.py`**: A Flask-based backend that serves the model to the web interface.
*   **`index_commerce.html`**: A clean user interface for making real-time predictions.
*   **`requirment.txt`**: List of dependencies needed to run the project.

---

##   Tech Stack
*   **Modeling:** Python, Scikit-Learn, Pandas, NumPy.
*   **Visualization:** Matplotlib, Seaborn.
*   **Deployment:** Flask (Backend), HTML/CSS (Frontend).
*   **Serialization:** Pickle (for saving the trained model).

---

##   Methodology
1.  **Exploratory Data Analysis (EDA):** Visualizing correlations between features like "Time on App" and "Length of Membership".
2.  **Model Training:** Implementing a Linear Regression model using the Ordinary Least Squares (OLS) method.
3.  **Evaluation:** Assessing performance using metrics such as Mean Absolute Error (MAE) and R-squared.
4.  **Deployment:** Creating a web form where users can input customer data to get an instant spending prediction.

---

##   How to Run
1.  Install the required libraries:
    ```bash
    pip install -r requirment.txt
    ```
2.  Run the Flask application:
    ```bash
    python app.py
    ```
3.  Open your browser and navigate to `http://127.0.0.1:5000` to interact with the model.

---

##   Insights
Based on the coefficients of our Linear Regression model, we can determine exactly how much each additional minute spent on the app or year of membership contributes to the total revenue.
