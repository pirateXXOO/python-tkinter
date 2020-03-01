from tkinter import *

root = Tk()

def test():
    if e1.get() == "Jack":
        print("Right")
        return True
    else:
        print("Wrong")
        e1.delete(0, END)
        return False


v = StringVar()

e1 = Entry(root, textvariable=v, validate="focusout", validatecommand=test)
e2 = Entry(root)
e1.grid(padx=10, pady=5)
e2.grid(padx=10, pady=5)


mainloop()
