import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

class EcoPredictor:
    """
    A simple ML predictor for EcoTrace environmental predictions
    """
    
    def __init__(self):
        self.model = None
        self.is_trained = False
        
    def prepare_sample_data(self):
        """
        Generate sample environmental data for demonstration
        """
        np.random.seed(42)
        n_samples = 1000
        
        # Sample features: temperature, humidity, carbon_emissions, energy_usage
        data = {
            'temperature': np.random.normal(25, 5, n_samples),
            'humidity': np.random.normal(60, 15, n_samples),
            'carbon_emissions': np.random.exponential(100, n_samples),
            'energy_usage': np.random.gamma(2, 50, n_samples)
        }
        
        df = pd.DataFrame(data)
        
        # Create a synthetic target: eco_score (higher is better)
        df['eco_score'] = (
            (30 - abs(df['temperature'] - 22)) * 2 +  # Optimal temp around 22°C
            (df['humidity'] / 2) +  # Higher humidity is better for some ecosystems
            (200 - df['carbon_emissions']) * 0.5 +  # Lower emissions are better
            (150 - df['energy_usage']) * 0.3  # Lower energy usage is better
        )
        
        # Add some noise
        df['eco_score'] += np.random.normal(0, 10, n_samples)
        
        return df
    
    def train(self, X=None, y=None):
        """
        Train the ML model
        """
        if X is None or y is None:
            # Use sample data if no data provided
            df = self.prepare_sample_data()
            X = df[['temperature', 'humidity', 'carbon_emissions', 'energy_usage']]
            y = df['eco_score']
        
        # Split the data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train the model
        self.model = LinearRegression()
        self.model.fit(X_train, y_train)
        
        # Evaluate the model
        y_pred = self.model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        self.is_trained = True
        
        return {
            'mse': mse,
            'r2_score': r2,
            'model_trained': True
        }
    
    def predict(self, features):
        """
        Make predictions using the trained model
        
        Args:
            features: dict or array-like with keys/order: 
                     ['temperature', 'humidity', 'carbon_emissions', 'energy_usage']
        """
        if not self.is_trained or self.model is None:
            raise ValueError("Model must be trained before making predictions")
        
        if isinstance(features, dict):
            # Convert dict to array in correct order
            feature_array = np.array([[
                features['temperature'],
                features['humidity'],
                features['carbon_emissions'],
                features['energy_usage']
            ]])
        else:
            feature_array = np.array(features).reshape(1, -1)
        
        prediction = self.model.predict(feature_array)[0]
        
        # Calculate eco rating (A-F scale)
        if prediction >= 80:
            rating = 'A'
        elif prediction >= 60:
            rating = 'B'
        elif prediction >= 40:
            rating = 'C'
        elif prediction >= 20:
            rating = 'D'
        else:
            rating = 'F'
        
        return {
            'eco_score': round(prediction, 2),
            'eco_rating': rating,
            'recommendations': self.get_recommendations(features, prediction)
        }
    
    def get_recommendations(self, features, score):
        """
        Generate recommendations based on the input features and score
        """
        recommendations = []
        
        if isinstance(features, dict):
            if features['carbon_emissions'] > 100:
                recommendations.append("Reduce carbon emissions by using renewable energy")
            if features['energy_usage'] > 100:
                recommendations.append("Optimize energy consumption with efficient appliances")
            if features['temperature'] > 26:
                recommendations.append("Improve insulation to reduce cooling needs")
        
        if score < 50:
            recommendations.append("Consider implementing sustainable practices")
        
        return recommendations
    
    def save_model(self, filepath='trained_model.pkl'):
        """
        Save the trained model to a file
        """
        if self.model is None:
            raise ValueError("No model to save. Train the model first.")
        
        joblib.dump(self.model, filepath)
        return f"Model saved to {filepath}"
    
    def load_model(self, filepath='trained_model.pkl'):
        """
        Load a trained model from a file
        """
        if os.path.exists(filepath):
            self.model = joblib.load(filepath)
            self.is_trained = True
            return f"Model loaded from {filepath}"
        else:
            raise FileNotFoundError(f"Model file {filepath} not found")

# Example usage
if __name__ == "__main__":
    # Create and train the predictor
    predictor = EcoPredictor()
    
    print("Training the model...")
    results = predictor.train()
    print(f"Training completed!")
    print(f"R² Score: {results['r2_score']:.3f}")
    print(f"MSE: {results['mse']:.3f}")
    
    # Make a sample prediction
    print("\nMaking a sample prediction...")
    sample_input = {
        'temperature': 24.5,
        'humidity': 65.0,
        'carbon_emissions': 85.0,
        'energy_usage': 75.0
    }
    
    prediction = predictor.predict(sample_input)
    print(f"Input: {sample_input}")
    print(f"Eco Score: {prediction['eco_score']}")
    print(f"Eco Rating: {prediction['eco_rating']}")
    print(f"Recommendations: {prediction['recommendations']}")