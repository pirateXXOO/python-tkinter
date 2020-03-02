from tkinter import *

root = Tk()

s1 = Scale(from_=0, to=42, tickinterval=5, resolution=5, length=200)
s1.pack()

s2 = Scale(from_=0, to=200, orient=HORIZONTAL, resolution=10, length=600)
s2.pack()


def show():
    print(s1.get(), s2.get())


Button(root, text="GetLocation", command=show).pack()
mainloop()
