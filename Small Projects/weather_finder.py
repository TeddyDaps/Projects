


import tkinter as tk
from tkinter import messagebox
import requests

#You need to, firstly, find the right API for the weather data and then use the script

# Function to fetch weather data from OpenWeatherMap API
def get_weather(address, city, postal_code):
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'  # Replace with your OpenWeatherMap API key
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{postal_code}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data['cod'] == 200:
            temperature = data['main']['temp']
            messagebox.showinfo("Weather Information", f"The temperature in {city} is {temperature} °C")
        else:
            messagebox.showerror("Error", f"Error fetching weather data: {data['message']}")
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching weather data: {str(e)}")

# Function to handle button click
def get_weather_click():
    address = address_entry.get()
    city = city_entry.get()
    postal_code = postal_code_entry.get()
    
    if not address or not city or not postal_code:
        messagebox.showerror("Error", "Please enter all fields")
        return
    
    get_weather(address, city, postal_code)

# Create main application window
root = tk.Tk()
root.title("Weather App")

# Create labels and entries for address, city, and postal code
tk.Label(root, text="Address:").grid(row=0, column=0, padx=10, pady=10)
address_entry = tk.Entry(root, width=30)
address_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="City:").grid(row=1, column=0, padx=10, pady=10)
city_entry = tk.Entry(root, width=30)
city_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Postal Code:").grid(row=2, column=0, padx=10, pady=10)
postal_code_entry = tk.Entry(root, width=30)
postal_code_entry.grid(row=2, column=1, padx=10, pady=10)

# Create button to fetch weather
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather_click)
get_weather_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
