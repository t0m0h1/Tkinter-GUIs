import tkinter as tk
import numpy as np

root = tk.Tk()
root.title("Expense Tracker")
root.resizable(False, False)

expense_list = []

def add_expenses():
    expenses = expenses_entry.get()
    expense_list.append(float(expenses))  # convert string to float before appending
    expenses_entry.delete(0, tk.END)
    print(expense_list)
    print(np.sum(expense_list))
    total_expenses_label.config(text=f"Total:  £ {np.sum(expense_list)}")
    total_expenses_label.grid(column=1, row=4)
    expenses_entry.grid(column=1, row=1)
    add_expenses_button.grid(column=1, row=3)
    return expense_list


def clear():
    total_expenses_label.config(text="Expenses: ")



add_expenses_label = tk.Label(root, text="Add Expenses :", font=("Helvetica", 16))
add_expenses_label.grid(column=1, row=0, pady=10)


total_expenses_label = tk.Label(root, text="", font=("Helvetica", 16))


expenses_entry = tk.Entry(root, font=("Helvetica", 16))
expenses_entry.grid(column=1, row=1, columnspan=2, pady=10)

add_expenses_button = tk.Button(root, text="Add", font=("Helvetica", 16), command=add_expenses)
add_expenses_button.grid(column=1, row=3)


clear_button = tk.Button(root, text="Clear", font=("Helvetica", 16), command=clear)
clear_button.grid(column=2, row=3)









root.mainloop()