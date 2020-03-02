from tkinter import *

root = Tk()

text = Text(root, width=30, height=10)
text.pack()

text.insert(INSERT, "I love \n")
text.insert(END, "You")


def show():
    print("Oh , I am clicked!")


b1 = Button(text, text="Click me", command=show)
text.window_create(INSERT, window=b1)

mainloop()
