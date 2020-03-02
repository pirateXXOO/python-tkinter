from tkinter import *

root = Tk()

text = Text(root, width=100, height=50)
text.pack()

text.insert(INSERT, "I love \n")
text.insert(END, "You")

photo = PhotoImage(file="18x.gif")


def show():
    text.image_create(END, image=photo)


b1 = Button(text, text="Click me", command=show)
text.window_create(INSERT, window=b1)

mainloop()
