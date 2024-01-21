# a very basic weather app using tkinter and bs4

import tkinter as tk
import requests
import bs4 as bs  # BeautifulSoup4
from configparser import ConfigParser # to read the api key from the config file


api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
api_key = "f16b10d7231140c354ada2715abc9b35"

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


def search():
    pass

def get_weather(city):
    result = requests.get(api_url.format(city, api_key))
    if result:
        print(result.content)
    else:
        return None

# create a label
label1 = tk.Label(root, text="Enter the city: ")
label1.pack()

# create an entry for the city
city_text = tk.StringVar()
city_entry = tk.Entry(root, textvariable=city_text)
city_entry.pack()

# create a button for searching the weather
search_button = tk.Button(root, text="", command=lambda: get_weather(city_text.get()))
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










root.mainloop()