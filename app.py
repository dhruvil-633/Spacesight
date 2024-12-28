from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS) for all routes

# Load the trained model and scaler
model = joblib.load('logistic_regression_model.pkl')
scaler = joblib.load('scaler.pkl')

# Route for the landing page
@app.route('/')
def index():
    return render_template('index.html')  # Landing page

# Route for the "Get Started" page
@app.route('/home')
def home():
    return render_template('home.html')  # Main page for input and interaction

# API Route for collision prediction
@app.route('/predict', methods=['POST'])
def predict():
    """
    API endpoint to receive input data from the frontend,
    run the model prediction, and return the result.
    """
    try:
        # Parse JSON data from the request
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
        scaled_data = scaler.transform(input_data)

        # Make the prediction
        collision_prob = model.predict_proba(scaled_data)[:, 1]
        collision_prediction = int(collision_prob >= 0.5)

        # Send back the prediction result
        result = "Collision will happen" if collision_prediction == 1 else "No collision detected"
        return jsonify({
            'prediction': collision_prediction,
            'result': result
        })

    except Exception as e:
        # Handle errors and send error response
        return jsonify({'error': str(e)}), 400

# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)
