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

city_text = tk.StringVar()
city_entry = tk.Entry(root, textvariable=city_text)
city_entry.pack()


search = tk.Button(root, text="Search Weather", command=lambda: get_weather(city_text.get()))
search.pack()






root.mainloop()