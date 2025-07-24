# EcoTrace 🌱

A web application for environmental tracking and prediction using machine learning.

## Features

- 🌍 Environmental data tracking and analysis
- 🤖 Machine Learning predictions for eco-scores
- 📊 RESTful API for data integration
- 🎯 Eco-rating system (A-F scale)
- 💡 Personalized recommendations

## Project Structure

```
EcoTrace/
├── backend/
│   ├── app.py              # Flask web application
│   └── ML/
│       ├── predictor.py    # ML prediction model
│       ├── train_model.py  # Model training script
│       └── trained_model.pkl # Trained model file
├── requirements.txt        # Python dependencies
├── .env                   # Environment variables
├── test_api.py           # API testing script
├── README.md             # This file
└── LICENSE               # License file
```

## Setup Instructions

### Prerequisites

- Python 3.12+ installed on your system
- Git (for version control)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd EcoTrace
   ```

2. **Create and activate virtual environment:**
   ```bash
   # Virtual environment is already created at .venv/
   # Activate it:
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Train the ML model:**
   ```bash
   cd backend
   python ML/train_model.py
   ```

5. **Run the application:**
   ```bash
   python backend/app.py
   ```

The application will be available at: `http://localhost:5000`

### Testing the API

Run the test script to verify everything works:
```bash
python test_api.py
```

## API Endpoints

### Base URL: `http://localhost:5000`

- **GET /** - Welcome message and API info
- **GET /api/health** - Health check endpoint
- **POST /api/predict** - ML prediction endpoint

### Example API Usage

**Prediction Request:**
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "temperature": 24.5,
    "humidity": 65.0,
    "carbon_emissions": 85.0,
    "energy_usage": 75.0
  }'
```

**Response:**
```json
{
  "success": true,
  "prediction": {
    "input_data": { ... },
    "prediction": "Sample prediction result",
    "confidence": 0.85
  }
}
```

## Development

### Environment Variables

Create a `.env` file with:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
FLASK_ENV=development
API_VERSION=1.0.0
```

### Code Formatting

Format code with Black:
```bash
black backend/
```

### Linting

Check code with Flake8:
```bash
flake8 backend/
```

### Testing

Run tests with pytest:
```bash
pytest
```

## Machine Learning Model

The ML model predicts eco-scores based on:
- Temperature (°C)
- Humidity (%)
- Carbon emissions (kg CO2)
- Energy usage (kWh)

**Output:**
- Eco Score (0-200+)
- Eco Rating (A-F)
- Personalized recommendations

### Model Performance
- R² Score: ~0.97
- Uses Linear Regression for simplicity
- Trained on synthetic environmental data

## Next Steps

1. 🎨 **Frontend Development**: Create a React/Vue.js frontend
2. 🗄️ **Database Integration**: Add PostgreSQL/SQLite for data persistence
3. 📈 **Advanced ML**: Implement more sophisticated models
4. 🔐 **Authentication**: Add user management and API keys
5. 📱 **Mobile App**: Develop mobile companion app
6. 🌐 **Deployment**: Deploy to cloud platforms (AWS, Azure, etc.)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or issues, please open an issue on GitHub.

---

**Happy coding! 🚀🌱**
