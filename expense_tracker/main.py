import tkinter as tk
import numpy as np
import sqlite3

# tkinter expense tracker: add expenses, view expenses, delete expenses, save expenses




# create the main window and set the title
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x400")
root.resizable(False, False)


# functions
def total_expenses():
    expense_list = []
    expense_list.append(float(expenses_entry.get()))
    total = np.sum(expense_list)
    total_expenses_label.config(text="£" + str(total))


# labels
expenses_label = tk.Label(root, text="Enter Expenses:", font=("Helvetica", 16))
total_expenses_label = tk.Label(root, text="Total Expenses:", font=("Helvetica", 16))

# grid the labels
expenses_label.grid(column=0, row=0)
total_expenses_label.grid(column=0, row=1)








expenses_entry = tk.Entry(root, font=("Helvetica", 16))
expenses_entry.grid(column=1, row=0)


submit_button = tk.Button(root, text="Submit", font=("Helvetica", 16), command=total_expenses)
submit_button.grid(column=0, row=2)








root.mainloop()

