# a very basic weather app using tkinter and bs4

import tkinter as tk
import requests
import bs4 as bs  # BeautifulSoup4

# create a window
root = tk.Tk()

# set the title
root.title("Weather App")

# set the size of the window
root.geometry("400x400")


def search():
    pass


# create a label
label1 = tk.Label(root, text="Enter the city: ")
label1.pack()

# create an entry for the city
city_text = tk.StringVar()
city_entry = tk.Entry(root, textvariable=city_text)
city_entry.pack()

# create a button for searching the weather
search_button = tk.Button(root, text="Search Weather", command=lambda: get_weather(city_text.get()))
search_button.pack()

# create a label for the weather
location_label = tk.Label(root, text="Location", font=("bold", 20))
location_label.pack()

image = tk.Label(root, bitmap="")





root.mainloop()