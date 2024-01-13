import tkinter as tk
#from PIL import ImageTk, Image
import sqlite3

root = tk.Tk()
root.title('Not sure yet')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("400x400")

# Create a database or connect to one
connection = sqlite3.connect('address_book.db')

# Create cursor
# A cursor is a control structure that enables traversal over the records in a database.
# Cursors facilitate subsequent processing in conjunction with the traversal, such as retrieval, addition and removal of database records.
c = connection.cursor()


#commit the changes to db
connection.commit()


root.mainloop()

