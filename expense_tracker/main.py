import tkinter as tk
import numpy as np

root = tk.Tk()
expense_list = []

def add_expenses():
    expenses = expenses_entry.get()
    expense_list.append(float(expenses))  # convert string to float before appending
    expenses_entry.delete(0, tk.END)
    print(expense_list)
    print(np.sum(expense_list))
    expenses_label.config(text=f"Expenses:  £ {np.sum(expense_list)}")
    expenses_label.grid(column=0, row=0)
    expenses_entry.grid(column=1, row=0)
    add_expenses_button.grid(column=1, row=3)
    return expense_list


def clear():
    expenses_label.config(text="Expenses: ")




expenses_label = tk.Label(root, text="Expenses: ", font=("Helvetica", 16))
expenses_label.grid(column=0, row=0)

expenses_entry = tk.Entry(root, font=("Helvetica", 16))
expenses_entry.grid(column=1, row=0)

add_expenses_button = tk.Button(root, text="Add", font=("Helvetica", 16), command=add_expenses)
add_expenses_button.grid(column=1, row=3)

total_expenses_label = tk.Label(root, text=f'{expense_list}', font=("Helvetica", 16))
total_expenses_label.grid(column=0, row=4)

clear_button = tk.Button(root, text="Clear", font=("Helvetica", 16), command=clear)
clear_button.grid(column=1, row=4)

root.mainloop()