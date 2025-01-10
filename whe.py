import requests
from tkinter import *
from tkinter import messagebox
import os

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city):
    api_key = "e047e900e2145cfef0cee860ad53546c"  # Replace with environment variable in production
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        weather = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
        return weather
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

# Function to display weather data in the GUI
def search_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name")
        return
    
    weather = get_weather(city)
    if weather:
        location_label["text"] = f"{weather['city']}, {weather['country']}"
        temperature_label["text"] = f"Temperature: {weather['temperature']}°C"
        description_label["text"] = f"Condition: {weather['description'].capitalize()}"
        humidity_label["text"] = f"Humidity: {weather['humidity']}%"
        wind_label["text"] = f"Wind Speed: {weather['wind_speed']} m/s"
    else:
        messagebox.showerror("Error", f"Could not find weather for '{city}'")

# Create main Tkinter app window
app = Tk()
app.title("Weather Dashboard")
app.geometry("400x300")
app.resizable(False, False)

# Input field for city name
city_entry = Entry(app, font=("Helvetica", 14))
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

# Search button
search_button = Button(app, text="Search Weather", font=("Helvetica", 14), command=search_weather)
search_button.pack(pady=10)

# Weather display labels
location_label = Label(app, text="Location", font=("Helvetica", 16, "bold"))
location_label.pack(pady=5)

temperature_label = Label(app, text="Temperature", font=("Helvetica", 14))
temperature_label.pack(pady=5)

description_label = Label(app, text="Condition", font=("Helvetica", 14))
description_label.pack(pady=5)

humidity_label = Label(app, text="Humidity", font=("Helvetica", 14))
humidity_label.pack(pady=5)

wind_label = Label(app, text="Wind Speed", font=("Helvetica", 14))
wind_label.pack(pady=5)

# Run the Tkinter app
app.mainloop()
