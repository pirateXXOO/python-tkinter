from tkinter import *

root = Tk()

GIRLS = ['Xi Shi', 'Diao Chan', 'Wang Zhaojun', 'Yang Yvhuan']

v = []

for girl in GIRLS:
    v.append(IntVar())
    b = Checkbutton(root, text=girl, variable=v[-1])
    b.pack(anchor=W)

mainloop()