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


def test2():
    print("????")


v = StringVar()

e1 = Entry(root, textvariable=v, validate="focusout", validatecommand=test, invalidcommand=test2)
e2 = Entry(root)
e1.grid(padx=10, pady=5)
e2.grid(padx=10, pady=5)


mainloop()
