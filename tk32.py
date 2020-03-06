from tkinter import *

root = Tk()

w = Canvas(root, width=200, height=100, background="red")
w.pack()

line1 = w.create_line(0, 50, 200, 50, fill="yellow")
line2 = w.create_line(100, 0, 100, 100, fill="blue", dash=(4, 4))
rect1 = w.create_rectangle(50, 25, 150, 75, fill="purple")

w.coords(line1, 0, 2, 200, 25)
w.itemconfig(rect1, fill="black")
w.delete(line2)

Button(root, text="Delete all", command=(lambda x=ALL: w.delete(x))).pack()

mainloop()
