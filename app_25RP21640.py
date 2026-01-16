from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)  # allow cross-origin requests for local testing

# Load the model
model = joblib.load('deployment/best_model.pkl')

# Load feature columns and class names
with open('deployment/feature_columns.txt', 'r') as f:
    feature_columns = [line.strip() for line in f.readlines()]

with open('deployment/class_names.txt', 'r') as f:
    class_names = [line.strip() for line in f.readlines()]


@app.route('/')
def home():
    # Serve index.html from same folder
    return send_file('index_25RP21640.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        # Check missing columns
        missing_cols = [col for col in feature_columns if col not in data]
        if missing_cols:
            return jsonify({'error': f'Missing columns: {missing_cols}'}), 400

        # Convert numeric features to float
        numeric_cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'ca']
        for col in numeric_cols:
            data[col] = float(data[col])

        # Convert boolean features
        bool_cols = ['fbs', 'exang']
        for col in bool_cols:
            val = data[col]
            if str(val).lower() in ['true', 'yes', '1']:
                data[col] = True
            else:
                data[col] = False

        # Create DataFrame
        input_df = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(input_df)[0]
        probabilities = model.predict_proba(input_df)[0] if hasattr(model, 'predict_proba') else None

        response = {
            'prediction': prediction,
            'probabilities': dict(zip(class_names, probabilities.tolist())) if probabilities is not None else None
        }

        return jsonify(response)

    except Exception as e:
        print("Predict error:", e)
        return jsonify({'error': str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
