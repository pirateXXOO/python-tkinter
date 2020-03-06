from tkinter import *

root = Tk()

m = PanedWindow(orient=VERTICAL)
m.pack(fill=BOTH, expand=1)

top = Label(m, text="top pend")
m.add(top)

bottom = Label(m, text="Button pane")
m.add(bottom)

mainloop()
