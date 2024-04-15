'''
   A simple GUI Weather Application using Python's Tkinter library.
   By: Rajat Gupta
       https://www.linkedin.com/in/rajat-gupta-21x/
       https://github.com/rajat-gupta-21/CodeWay/tree/main/
'''
import tkinter as tk
import requests
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import ttkbootstrap as ttkb

def get_weather(city):
    try:
        API_KEY = '507680b93854040465ca382203b0149c'
        URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        res = requests.get(URL)

        if res.status_code == 404:
            messagebox.showerror("Error","No such city")
            return None

        # parsing json to get weather info
        weather = res.json()
        icon_id = weather['weather'][0]['icon']
        temperature = weather['main']['temp'] - 273.15
        humidity = weather['main']['humidity']
        wind_speed = weather['wind']['speed']
        description = weather['weather'][0]['description']
        city = weather['name']
        country = weather['sys']['country']

        # get icon URL and return all weather info
        icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
        return (icon_url, temperature, humidity,wind_speed,description, city, country)
    except:
        return None

def search():
    try:
        city = city_entry.get()
        result = get_weather(city)
        if result is None:
            return

        # if city is found
        icon_url, temperature, humidity,wind_speed,description, city, country = result
        location_label.configure(text=f"{city}, {country}")

        # icon
        icon_image = Image.open(requests.get(icon_url,stream=True).raw)
        icon = ImageTk.PhotoImage(icon_image)
        icon_label.configure(image = icon)
        icon_label.icon_image = icon

        # temp, humidity, wind speed, description
        temp_label.configure(text = f"Temperature: {temperature:.2f}°C")
        humidity_label.configure(text = f"Humidity: {humidity}")
        windspd_label.configure(text=f"Wind Speed: {wind_speed}")
        description_label.configure(text = f"Description: {description}")

    except:
        return

def on_search_icon_click(event):
    search()

def clear_default_text(event):
    if city_entry.get() == "Enter region name...":
        city_entry.delete(0, tk.END)
        city_entry.config()

root = ttkb.Window(themename="morph")
root.title("Weather Forecast App by Rajat Gupta")
root.geometry("450x450")
root.minsize(450,450)
root.maxsize(450,450)
# Set custom icon
root.iconbitmap('weather_app.ico')

# entry widget -> city name
search_frame = ttkb.Frame(root)
search_frame.pack(pady=10)

default_text = "Enter region name..."
city_entry = ttkb.Entry(search_frame, font="Arial 18 bold")
city_entry.insert(0, default_text)
city_entry.bind("<FocusIn>", clear_default_text)
city_entry.pack(side=tk.LEFT)

# Search icon
search_icon = tk.PhotoImage(file="search_icon.png")
search_icon_label = ttkb.Label(search_frame, image=search_icon)
search_icon_label.pack(side=tk.LEFT, padx=5)

# Bind the on_search_icon_click function to the search icon label
search_icon_label.bind("<Button-1>", on_search_icon_click)

# label widget -> to show city/country name
location_label = tk.Label(root, font="Arial 25 bold")
location_label.pack(pady=20)

# label widget -> to show weather icon
icon_label = tk.Label(root)
icon_label.pack()

# label widget -> to show temperature
temp_label = tk.Label(root, font="Arial 15 bold")
temp_label.pack()

# label widget -> to show wind speed
windspd_label = tk.Label(root, font="Arial 15 bold")
windspd_label.pack()

# label widget -> to show humidity
humidity_label = tk.Label(root, font="Arial 15 bold")
humidity_label.pack()

# label widget -> to show description
description_label = tk.Label(root, font="Arial 15 bold")
description_label.pack()

# label widget -> to show weather description
weather_label = tk.Label(root, font="Arial 20 bold")
weather_label.pack()

root.mainloop()
