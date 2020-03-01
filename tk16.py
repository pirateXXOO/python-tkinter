from tkinter import *

root = Tk()


def test(content, reason, name):
    if content == 'Jack':
        print("Right")
        print(content, reason, name)
        return True
    else:
        print("Wrong")
        print(content, reason, name)
        return False


v = StringVar()

testCMD = root.register(test)
e1 = Entry(root, textvariable=v, validate="focusout", validatecommand=(testCMD, '%P', '%v', '%W'))
e2 = Entry(root)
e1.grid(padx=10, pady=5)
e2.grid(padx=10, pady=5)


mainloop()
