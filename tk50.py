from tkinter import *

root = Tk()


def create():
    top = Toplevel()
    top.title("Hello")

    msg = Message(top, text="I love python")
    msg.pack()


Button(root, text="Create top window", command=create).pack()

mainloop()
