from tkinter import *

root = Tk()


def callback():
    print("Hello")


menuBar = Menu(root)

menuBar = Menu(menuBar)
menuBar.add_command(label="undo", command=callback)
menuBar.add_command(label="redo", command=root.quit)

frame = Frame(root, width=512, height=512)
frame.pack()


def popup(event):
    menuBar.post(event.x_root, event.y_root)


frame.bind("<Button-3>", popup)

mainloop()
