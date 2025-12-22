from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)  

model = joblib.load("ecommerce_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    print("Received:", data)

    required_features = ["quantity", "unit_price", "discount", "category_code"]
    if not all(f in data for f in required_features):
        return jsonify({"error": "Missing features"}), 400

    X = np.array([[
        data["quantity"],
        data["unit_price"],
        data["discount"],
        data["category_code"]
    ]])
    
    prediction = model.predict(X)
    return jsonify({"predicted_revenue": float(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
