from tkinter import *

root = Tk()


def callback():
    print("Hello")


menuBar = Menu(root)


fileMenu = Menu(menuBar)
fileMenu.add_checkbutton(label="open", command=callback)
fileMenu.add_checkbutton(label="save", command=callback)
fileMenu.add_separator()
fileMenu.add_command(label="quit", command=root.quit)
menuBar.add_cascade(label="file", menu=fileMenu)

editMenu = Menu(menuBar, tearoff=False)
editMenu.add_command(label="cut", command=callback)
editMenu.add_command(label="copy", command=callback)
editMenu.add_command(label="paste", command=callback)
menuBar.add_cascade(label="edit", menu=editMenu)
root.config(menu=menuBar)

mainloop()
