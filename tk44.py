from tkinter import *

root = Tk()

w1 = Message(root, text="This is a message", width=100)
w1.pack()

w2 = Message(root, text="This is a lonnnnnnnn\nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnng message", width=100)
w2.pack()

mainloop()
