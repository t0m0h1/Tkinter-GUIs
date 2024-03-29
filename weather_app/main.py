# a very basic weather app using tkinter and bs4

import tkinter as tk
from tkinter import messagebox # to show error message later on
import requests
import bs4 as bs  # BeautifulSoup4
from configparser import ConfigParser # to read the api key from the config file


api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


# config file
config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
section = config["openweathermap"]
api_key = section["api_key"]




# create a window
root = tk.Tk()

# set the title 
root.title("Weather App")

# set the size of the window
root.geometry("400x400")


def get_weather(city):
    result = requests.get(api_url.format(city, api_key))
    if result.status_code != 200:  # If the status code is not 200, the request was not successful
        raise Exception(f"Error: Received status code {result.status_code} from OpenWeatherMap API")
    json = result.json()
    # city, country, temp_celsius, temp_fahrenheit, icon, weather etc
    city = json["name"]
    country = json["sys"]["country"]
    temp_kelvin = json["main"]["temp"] # temperature in kelvin to be converted to celsius
    temp_celsius = temp_kelvin - 273.15
    temp_farenheit = (temp_kelvin - 273.15) * 9/5 + 32 # temperature conversion formula
    icon = json["weather"][0]["icon"]
    weather = json["weather"][0]["main"]
    final = (city, country, temp_celsius, temp_farenheit, icon, weather)
    return final # return the tuple


def search():
    city = city_text.get()
    try:
        weather = get_weather(city)
        location_label["text"] = f"{weather[0]}, {weather[1]}"
        image["bitmap"] = "../images/{}.png".format(weather[4])
        temperature_label["text"] = f"{weather[2]:.2f}°C, {weather[3]:.2f}°F"
        weather_label["text"] = weather[5]
    except Exception as e:
        messagebox.showerror("Error", str(e))



# create a label
label1 = tk.Label(root, text="Enter the city: ")
label1.pack()

# create an entry for the city
city_text = tk.StringVar()
city_entry = tk.Entry(root, textvariable=city_text)
city_entry.pack()

# create a button for searching the weather
search_button = tk.Button(root, text="Search", command=search)
search_button.pack()

# create a label for the weather
location_label = tk.Label(root, text="", font=("bold", 20))
location_label.pack()

# create a label for the weather image
image = tk.Label(root, bitmap="")
image.pack()


# create a label for the temperature
temperature_label = tk.Label(root, text="", font=("bold", 15))
temperature_label.pack()

# create a label for the weather condition
weather_label = tk.Label(root, text="")
weather_label.pack()

# check that the api key is correctly read from the config file
api_key = section["api_key"]
print(api_key)


# run the app
root.mainloop()