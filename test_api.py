"""
Test script for EcoTrace API
"""

import requests
import json

# API base URL
BASE_URL = "http://127.0.0.1:5000"

def test_home_endpoint():
    """Test the home endpoint"""
    print("🏠 Testing home endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Home endpoint works!")
            print(f"   Message: {data['message']}")
            print(f"   Version: {data['version']}")
        else:
            print(f"❌ Home endpoint failed with status {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing home endpoint: {e}")

def test_health_endpoint():
    """Test the health check endpoint"""
    print("\n🏥 Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/api/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health endpoint works!")
            print(f"   Status: {data['status']}")
            print(f"   Service: {data['service']}")
        else:
            print(f"❌ Health endpoint failed with status {response.status_code}")
    except Exception as e:
        print(f"❌ Error testing health endpoint: {e}")

def test_predict_endpoint():
    """Test the prediction endpoint"""
    print("\n🔮 Testing prediction endpoint...")
    try:
        # Sample data for prediction
        sample_data = {
            "temperature": 24.5,
            "humidity": 65.0,
            "carbon_emissions": 85.0,
            "energy_usage": 75.0
        }
        
        response = requests.post(
            f"{BASE_URL}/api/predict",
            json=sample_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Prediction endpoint works!")
            print(f"   Success: {data['success']}")
            print(f"   Input: {data['prediction']['input_data']}")
            print(f"   Prediction: {data['prediction']['prediction']}")
            print(f"   Confidence: {data['prediction']['confidence']}")
        else:
            print(f"❌ Prediction endpoint failed with status {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Error testing prediction endpoint: {e}")

def main():
    """Main test function"""
    print("🧪 EcoTrace API Testing")
    print("=" * 30)
    
    test_home_endpoint()
    test_health_endpoint()
    test_predict_endpoint()
    
    print("\n🎉 API testing completed!")
    print("\n💡 Next steps:")
    print("   1. Integrate the ML model with the /api/predict endpoint")
    print("   2. Add more API endpoints as needed")
    print("   3. Create a frontend to interact with the API")
    print("   4. Add database integration if needed")

if __name__ == "__main__":
    main()
