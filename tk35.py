from tkinter import *
import math as m

root = Tk()

w = Canvas(root, width=200, height=100, background="red")
w.pack()

center_x = 100
center_y = 50
r = 50

points = [
    # Left up point
    center_x - int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    # Right up point
    center_x + int(r * m.sin(2 * m.pi / 5)),
    center_y - int(r * m.cos(2 * m.pi / 5)),
    # left down point
    center_x - int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5)),
    # top point
    center_x,
    center_y - r,
    # right down point
    center_x + int(r * m.sin(m.pi / 5)),
    center_y + int(r * m.cos(m.pi / 5))


]

w.create_polygon(points, outline="green", fill="yellow")



mainloop()
