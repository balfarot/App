import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from openpyxl import workbook
from openpyxl import load_workbook
import pandas as pd
from PIL import Image, ImageTk

# creating tkinter window
root = tk.Tk()
root.title('Lottery')
root.geometry("500x500")
root.resizable(0, 0)
root.grid_columnconfigure(1, weight=1)
# You can use grid_columnconfigure to show empty columns. This shows column 1
# By default, the weight of each column or row is 0, meaning don't expand to fill space.

# add image
picture = Image.open("csumb1.png")
resizedpic = picture.resize((100, 100), Image.ANTIALIAS)
resizedpic1 = ImageTk.PhotoImage(resizedpic)
label = Label(root, image=resizedpic1)
label.place(x=200, y=10)


# first button
def apple():
    data = pd.read_excel("csumb.xlsx")
    df = pd.DataFrame(data, columns=['Calendar'])
    lb.config(text=df)


b1 = tk.Button(text="Calendar", font=("Arial", 15), bg="#A3E4D7",
               command=apple)
b1.place(x=110, y=70)
lb = tk.Label(font=("Arial", 10), text=" ", justify="left").place(x=125, y=130)


# creating another button
def apple1():
    data1 = pd.read_excel("hello1.xlsx")
    col = pd.DataFrame(data1, columns=['StudentName'])
    lb.config(text=col)


b2 = tk.Button(text="Student", font=("Arial", 15), bg="#A3E4D7",
               command=apple1)
b2.place(x=220, y=70)
lb = tk.Label(font=("Arial", 10), text=" ", justify="left")
lb.place(x=30, y=130)

b2 = tk.Button(text="quit", font=("Arial", 15), bg="#A3E4D7",
               command=exit)
b2.place(x=350, y=80)
lb = tk.Label(font=("Arial", 10), text=" ", justify="right")
lb.place(x=80, y=130)

tk.mainloop()
