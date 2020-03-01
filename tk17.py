from tkinter import *

root = Tk()

v1 = StringVar()
v2 = StringVar()
v3 = StringVar()


def test(content):
    return content.isdigit()


testCMD = root.register(test)
e1 = Entry(root, textvariable=v1, validate="key", validatecommand=(testCMD, '%P')).grid(row=0, column=0)
Label(root, text="+").grid(row=0, column=1)
e2 = Entry(root, textvariable=v2, validate="key", validatecommand=(testCMD, '%P')).grid(row=0, column=2)
Label(root, text="=").grid(row=0, column=3)
e3 = Entry(root, textvariable=v3, state='readonly').grid(row=0, column=4)


def calc():
    result = int(v1.get()) + int(v2.get())
    v3.set(str(result))


Button(root, text="Calculate", command=calc).grid(row=1, column=2)

mainloop()
