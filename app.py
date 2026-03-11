import logging
import pandas as pd
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

model = joblib.load("model_data/boston_housing_prediction.joblib")

@app.route("/")
def home():
    return "Boston Housing Prediction API"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        json_data = request.get_json()
        logging.info(f"Input data: {json_data}")

        data = pd.DataFrame(json_data)
        prediction = model.predict(data)

        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        logging.error(str(e))
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
