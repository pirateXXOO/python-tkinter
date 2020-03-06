from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
root = Tk()


def callback():
    fileName = colorchooser.askcolor()
    print(fileName)


Button(root, text="chose color", command=callback).pack()


mainloop()
