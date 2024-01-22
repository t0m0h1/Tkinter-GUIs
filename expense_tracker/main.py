import tkinter as tk
import numpy as np
import sqlite3

# tkinter expense tracker: add expenses, view expenses, delete expenses, save expenses




# create the main window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")


expense_list = []

expenses_label = tk.Label(root, text="Enter Expenses:", font=("Helvetica", 16))
expenses_label.grid(column=0, row=0)





root.mainloop()

