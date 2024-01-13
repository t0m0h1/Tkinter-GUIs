import sqlite_utils
import tkinter as tk
from tkinter import messagebox

# Initialize the SQLite database
db = sqlite_utils.Database("my_database.db")
table = db.table("my_table", pk="id")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Database")
root.geometry("400x400")

# Create a form to input data
entry = tk.Entry(root)
entry.pack()

def submit_data():
    # When the form is submitted, insert the data into the SQLite database
    table.insert({"data": entry.get()})
    # Show a success message
    messagebox.showinfo("Success", "Data inserted successfully")

def show_data():
    # Get all the data from the SQLite database
    data = table.all()
    # Show the data in a message box
    messagebox.showinfo("Data", data)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.pack()

# Create a show button
show_button = tk.Button(root, text="Show", command=show_data)
show_button.grid(column=0, row=1)

root.mainloop()




