from tkinter import *

root = Tk()


def callback():
    print("Hello")


mb = Menubutton(root, text="click me", relief=RAISED)
mb.pack()


openVar = IntVar()
saveVar = IntVar()
quitVar = IntVar()

fileMenu = Menu(mb, tearoff=False)
fileMenu.add_command(label="open", command=callback)
fileMenu.add_command(label="save", command=callback)
fileMenu.add_separator()
fileMenu.add_checkbutton(label="quit", command=root.quit, variable=quitVar)

mb.config(menu=fileMenu)

mainloop()
