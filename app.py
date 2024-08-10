from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the trained model and scaler
model = joblib.load('logistic_regression_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        # Extract input features
        x_sim = float(data['x_sim'])
        y_sim = float(data['y_sim'])
        z_sim = float(data['z_sim'])
        Vx_sim = float(data['Vx_sim'])
        Vy_sim = float(data['Vy_sim'])
        Vz_sim = float(data['Vz_sim'])

        # Prepare the data for prediction
        input_data = pd.DataFrame({
            'x_sim': [x_sim],
            'y_sim': [y_sim],
            'z_sim': [z_sim],
            'Vx_sim': [Vx_sim],
            'Vy_sim': [Vy_sim],
            'Vz_sim': [Vz_sim]
        })

        # Scale the input data
        input_data = scaler.transform(input_data)

        # Make the prediction
        collision_prob = model.predict_proba(input_data)[:, 1]
        collision_prediction = int(collision_prob >= 0.5)

        # Send back the prediction result
        result = "collision will happen" if collision_prediction == 1 else "The collision will not happen"
        return jsonify({'prediction': collision_prediction, 'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
