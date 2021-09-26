# World Weather Analysis

## Overview

### Task
Collect and analyze weather data across cities worldwide

### Purpose
PlanMyTrip will use the data to recommend ideal hotels based on clients' weather preferences.

### Method 
Create a Pandas DataFrame with 500 or more of the world's unique cities and their weather data in real time. This process will entail collecting, analyzing, and visualizing the data.

## Analysis

### Collect the Data

- Use the NumPy module to generate more than 1,500 random latitudes and longitudes.
- Use the [citipy](https://pypi.org/project/citipy/) module to list the nearest city to the latitudes and longitudes.
- Use the [OpenWeather](https://openweathermap.org/api) API to request the current weather data from each unique city in your list.
- Parse the JSON data from the API request.
- Collect the following data from the JSON file and add it to a DataFrame:
    - City, country, and date
    - Latitude and longitude
    - Maximum temperature
    - Humidity
    - Cloudiness
    - Wind speed

### Exploratory Analysis with Visualization

- Create scatter plots of weather data 
- Determine the correlations
- Create series of heatmaps using Google Maps and Places API for:
    - Latitude and temperature
    - Latitude and humidity
    - Latitude and cloudiness
    - Latitude and wind speed

### Visual Travel Data

- Create a heatmap with pop-up markers that can display information on specific cities based on a customer's travel preferences.

### Jupyter Notebooks
The Jupyter Notebooks for the Module 6 Lesson are listed below:
- [WeatherPy](WeatherPy.ipynb)
- [VacationPy](VacationPy.ipynb)
- [API_Practice](API_Practice.ipynb)
