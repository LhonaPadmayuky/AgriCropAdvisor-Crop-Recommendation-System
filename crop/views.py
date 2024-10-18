from django.shortcuts import render, HttpResponse
import pickle
import numpy as np
import requests
from datetime import datetime, timedelta

# Load the trained RandomForest model
with open('L:/crop/croprecommendation/crop_recommendation/crop/model/RandomForest.pkl', 'rb') as file:
    model = pickle.load(file)

# Home Page View
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def crops(request):
    return render(request, 'crops.html')

# Crop Prediction View
def predict_crop(request):
    if request.method == 'POST':
        # Extracting input values from form
        nitrogen = float(request.POST.get('nitrogen'))
        phosphorus = float(request.POST.get('phosphorus'))
        potassium = float(request.POST.get('potassium'))
        temperature = float(request.POST.get('temperature'))
        humidity = float(request.POST.get('humidity'))
        ph = float(request.POST.get('ph'))
        rainfall = float(request.POST.get('rainfall'))

        # Input features arranged in the required format for prediction
        input_features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph, rainfall]])

        # Making a prediction
        prediction = model.predict(input_features)[0]

        # Sending the result back to the template
        return render(request, 'result.html', {'prediction': prediction})

    return render(request, 'index.html')

# OpenWeather API key
api_key = '978e17cabcd7846624f87ec293e4282f'

# Function to get latitude and longitude for a given district and state
def get_lat_lon(district, state):
    geocode_url = f'http://api.openweathermap.org/geo/1.0/direct?q={district},{state}&appid={api_key}'
    response = requests.get(geocode_url)
    data = response.json()
    
    if len(data) > 0:
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        return latitude, longitude
    else:
        return None, None

# Function to fetch historical weather data for the last few months
def get_historical_weather(lat, lon):
    end_date = datetime.now()
    num_days = 90  # Fetch for the last 90 days (about 3 months)
    weather_data = []

    for i in range(num_days):
        # Subtract days from the current date to get historical dates
        historical_date = end_date - timedelta(days=i)
        unix_timestamp = int(historical_date.timestamp())
        
        # Historical weather data API request
        one_call_url = f'http://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={unix_timestamp}&appid=fdcb636d0b28f7bcc86ec8cb849e199a'
        response = requests.get(one_call_url)
        data = response.json()
        
        if 'current' in data:
            # Store daily temperature and rainfall data
            temperature = data['current']['temp'] - 273.15  # Convert from Kelvin to Celsius
            rainfall = data['current'].get('rain', {}).get('1h', 0)  # Get rainfall, default to 0 if not available
            
            weather_data.append({'temperature': temperature, 'rainfall': rainfall})

    return weather_data

# Function to compute averages
def compute_average_weather(weather_data):
    temperatures = [day['temperature'] for day in weather_data]
    rainfalls = [day['rainfall'] for day in weather_data]
    
    avg_temperature = np.mean(temperatures) if temperatures else 0
    avg_rainfall = np.mean(rainfalls) if rainfalls else 0
    
    return avg_temperature, avg_rainfall

# Crop Recommendation View (Uses OpenWeather API and historical data)
def recommend_crop(request):
    if request.method == 'POST': 
        district = request.POST.get('district')
        state = request.POST.get('state')
        nitrogen = float(request.POST.get('nitrogen'))
        phosphorus = float(request.POST.get('phosphorus'))
        potassium = float(request.POST.get('potassium'))
        ph = float(request.POST.get('ph'))
        humidity = float(request.POST.get('humidity'))

        # Get the latitude and longitude for the district and state
        lat, lon = get_lat_lon(district, state)
        
        if lat is None or lon is None:
            return render(request, 'recommend.html', {'error': "Invalid location. Please check the district and state names."})
        
        # Fetch historical weather data for the last few months
        weather_data = get_historical_weather(lat, lon)
        avg_temperature, avg_rainfall = compute_average_weather(weather_data)
        
        # Prepare input for the model using soil and weather data
        input_features = np.array([[nitrogen, phosphorus, potassium, avg_temperature, humidity, ph, avg_rainfall]])

        # Make multiple crop predictions using the trained model
        probabilities = model.predict_proba(input_features)[0]  # Get prediction probabilities for each crop

        # Get top N crops based on probabilities
        top_n = 5  # You can change this number based on how many crops you want to recommend
        crops_indices = np.argsort(probabilities)[-top_n:][::-1]  # Get indices of the top N crops
        recommended_crops = [model.classes_[index] for index in crops_indices]  # Get crop names

        # Send the weather data and predicted crops to the result template
        return render(request, 'recommend_result.html', {
            'weather': {'temperature': avg_temperature, 'rainfall': avg_rainfall},
            'crops': recommended_crops
        })

    # If the request method is GET, display the recommendation form
    return render(request, 'recommend.html')
