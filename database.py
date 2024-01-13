import sqlite_utils
import tkinter as tk
from tkinter import messagebox

# Initialize the SQLite database
db = sqlite_utils.Database("my_database.db")
table = db.table("my_table", pk="id")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Database App")

# Create a form to input data
entry = tk.Entry(root)
entry.grid(column=0, row=0, columnspan=2)

def submit_data():
    # When the form is submitted, insert the data into the SQLite database
    table.insert({"data": entry.get()})
    # Show a success message
    messagebox.showinfo(f"Success, {entry.get()} has been added to the database")


def show_data():
    # Get all the data from the SQLite database
    data = table.rows
    data_str = "\n".join(str(row) for row in data)
    # Show the data in a message box
    messagebox.showinfo("Data", data_str)


def delete_data():
    # Prompt the user for confirmation before deleting the data
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to delete all data?")
    if confirm:
        # Delete the data from the SQLite database
        rows_to_delete = list(table.rows)
        table.delete(rows_to_delete)
        # Show a success message
        messagebox.showinfo("Success", "Data has been deleted")
    

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(column=1, row=1)

# Create a show button
show_button = tk.Button(root, text="Show", command=show_data)
show_button.grid(column=1, row=2)

# Create a clear button
clear_button = tk.Button(root, text="Clear", command=lambda: entry.delete(0, tk.END))
clear_button.grid(column=1, row=3)

# Create a delete button
delete_button = tk.Button(root, text="Delete", command=delete_data)
delete_button.grid(column=1, row=4)

root.mainloop()




