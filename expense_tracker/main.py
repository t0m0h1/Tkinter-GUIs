import tkinter as tk
import numpy as np

root = tk.Tk()
root.geometry("250x200")
root.title("Expense Tracker")
root.resizable(False, False)

expense_list = []

def add_expenses():
    expenses = expenses_entry.get()
    expense_list.append(float(expenses))  # convert string to float before appending
    expenses_entry.delete(0, tk.END)
    print(expense_list)
    print(np.sum(expense_list))
    expenses_label.config(text=f"Expenses:  £ {np.sum(expense_list)}")
    expenses_label.grid(column=0, row=4)
    expenses_entry.grid(column=1, row=0)
    add_expenses_button.grid(column=1, row=3)
    return expense_list


def clear():
    expenses_label.config(text="Expenses: ")




expenses_label = tk.Label(root, text="", font=("Helvetica", 16))


expenses_entry = tk.Entry(root, font=("Helvetica", 16))
expenses_entry.grid(column=1, row=0, columnspan=2)

add_expenses_button = tk.Button(root, text="Add", font=("Helvetica", 16), command=add_expenses)
add_expenses_button.grid(column=1, row=3)


clear_button = tk.Button(root, text="Clear", font=("Helvetica", 16), command=clear)
clear_button.grid(column=1, row=4)

root.mainloop()