from tkinter import *

root = Tk()


def callback():
    print("Hello")


menuBar = Menu(root)

openVar = IntVar()
saveVar = IntVar()
quitVar = IntVar()

fileMenu = Menu(menuBar)
fileMenu.add_checkbutton(label="open", command=callback, variable=openVar)
fileMenu.add_checkbutton(label="save", command=callback, variable=saveVar)
fileMenu.add_separator()
fileMenu.add_checkbutton(label="quit", command=root.quit, variable=quitVar)
menuBar.add_cascade(label="file", menu=fileMenu)

editVar = IntVar()

editMenu = Menu(menuBar, tearoff=False)
editMenu.add_radiobutton(label="cut", command=callback, variable=editVar, value=1)
editMenu.add_radiobutton(label="copy", command=callback, variable=editVar, value=2)
editMenu.add_radiobutton(label="paste", command=callback, variable=editVar, value=3)
menuBar.add_cascade(label="edit", menu=editMenu)
root.config(menu=menuBar)

mainloop()
