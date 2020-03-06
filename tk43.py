from tkinter import *

OPTIONS = [
    "JIFEJ",
    "JFEI",
    "LJIFEOJOW",
    "JFOEIOWJF",
    "JFOEJOWJIEWO"
]

root = Tk()

variable = StringVar()
variable.set(OPTIONS[0])

w = OptionMenu(root, variable, *OPTIONS)
w.pack()
mainloop()
