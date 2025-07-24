from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
app.config['DEBUG'] = True

@app.route('/')
def home():
    """Home route for EcoTrace API"""
    return jsonify({
        'message': 'Welcome to EcoTrace API',
        'version': '1.0.0',
        'status': 'running'
    })

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'EcoTrace Backend'
    })

@app.route('/api/predict', methods=['POST'])
def predict():
    """Prediction endpoint for ML model"""
    try:
        data = request.get_json()
        
        # TODO: Implement your ML prediction logic here
        # For now, return a sample response
        prediction = {
            'input_data': data,
            'prediction': 'Sample prediction result',
            'confidence': 0.85
        }
        
        return jsonify({
            'success': True,
            'prediction': prediction
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)