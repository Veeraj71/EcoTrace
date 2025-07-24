"""
Training script for EcoTrace ML model
"""

import sys
import os

# Add the parent directory to the path so we can import from ML module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ML.predictor import EcoPredictor

def main():
    """
    Main training function
    """
    print("🌱 EcoTrace Model Training")
    print("=" * 30)
    
    # Initialize the predictor
    predictor = EcoPredictor()
    
    print("📊 Preparing sample environmental data...")
    sample_data = predictor.prepare_sample_data()
    print(f"✅ Generated {len(sample_data)} samples")
    print(f"📈 Features: {list(sample_data.columns[:-1])}")
    print(f"🎯 Target: eco_score")
    
    print("\n🚀 Training the model...")
    results = predictor.train()
    
    print("\n📊 Training Results:")
    print(f"✅ Model trained successfully!")
    print(f"📊 R² Score: {results['r2_score']:.4f}")
    print(f"📉 MSE: {results['mse']:.4f}")
    
    print("\n💾 Saving the model...")
    model_path = os.path.join(os.path.dirname(__file__), 'trained_model.pkl')
    save_result = predictor.save_model(model_path)
    print(f"✅ {save_result}")
    
    print("\n🧪 Testing the model with sample predictions...")
    
    # Test cases
    test_cases = [
        {
            'name': 'Eco-friendly scenario',
            'data': {
                'temperature': 22.0,
                'humidity': 65.0,
                'carbon_emissions': 50.0,
                'energy_usage': 60.0
            }
        },
        {
            'name': 'High emissions scenario',
            'data': {
                'temperature': 28.0,
                'humidity': 45.0,
                'carbon_emissions': 150.0,
                'energy_usage': 120.0
            }
        },
        {
            'name': 'Average scenario',
            'data': {
                'temperature': 24.0,
                'humidity': 60.0,
                'carbon_emissions': 100.0,
                'energy_usage': 85.0
            }
        }
    ]
    
    for i, test_case in enumerate(test_cases, 1):
        print(f"\n🔬 Test Case {i}: {test_case['name']}")
        prediction = predictor.predict(test_case['data'])
        
        print(f"   📊 Eco Score: {prediction['eco_score']}")
        print(f"   🏆 Eco Rating: {prediction['eco_rating']}")
        if prediction['recommendations']:
            print(f"   💡 Recommendations:")
            for rec in prediction['recommendations']:
                print(f"      • {rec}")
        else:
            print(f"   ✅ No recommendations needed - good job!")
    
    print("\n🎉 Training completed successfully!")
    print("🚀 You can now use the model in your Flask application!")

if __name__ == "__main__":
    main()