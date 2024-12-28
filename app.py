from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for all routes

# Define paths for the model and scaler files
MODEL_PATH = "model/logistic_regression_model.pkl"
SCALER_PATH = "model/scaler.pkl"

# Load the trained model and scaler
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("Model and scaler loaded successfully.")
except Exception as e:
    print(f"Error loading model or scaler: {e}")
    model = None
    scaler = None

# Route for the landing page
@app.route('/')
def index():
    """Render the landing page."""
    return render_template('index.html')

# Route for the "Get Started" page
@app.route('/home')
def home():
    """Render the main page for input and interaction."""
    return render_template('home.html')

# API Route for collision prediction
@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint to receive input data from the frontend,
    run the model prediction, and return the result.
    """
    if not model or not scaler:
        return jsonify({'error': 'Model or scaler is not loaded properly'}), 500

    try:
        # Parse JSON data from the request
        data = request.get_json()

        # Validate and extract input features from the request data
        required_fields = ['x_sim', 'y_sim', 'z_sim', 'Vx_sim', 'Vy_sim', 'Vz_sim']
        if not all(field in data for field in required_fields):
            return jsonify({'error': 'Missing required input fields'}), 400

        # Extract input features
        x_sim = float(data['x_sim'])
        y_sim = float(data['y_sim'])
        z_sim = float(data['z_sim'])
        Vx_sim = float(data['Vx_sim'])
        Vy_sim = float(data['Vy_sim'])
        Vz_sim = float(data['Vz_sim'])

        # Prepare the input data for prediction
        input_data = pd.DataFrame({
            'x_sim': [x_sim],
            'y_sim': [y_sim],
            'z_sim': [z_sim],
            'Vx_sim': [Vx_sim],
            'Vy_sim': [Vy_sim],
            'Vz_sim': [Vz_sim]
        })

        # Scale the input data using the loaded scaler
        scaled_data = scaler.transform(input_data)

        # Make the collision prediction
        collision_prob = model.predict_proba(scaled_data)[:, 1]
        collision_prediction = 1 if collision_prob >= 0.5 else 0

        # Determine the result message
        result_message = "Collision will happen" if collision_prediction == 1 else "No collision detected"

        return jsonify({
            'prediction': collision_prediction,
            'result': result_message
        })

    except Exception as e:
        # Handle any errors and send an error response
        return jsonify({'error': str(e)}), 400

# Main function to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
