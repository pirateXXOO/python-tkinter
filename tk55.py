from tkinter import *

root = Tk()


Label(root, text="username").grid(row=0, sticky=W)
Label(root, text="password").grid(row=1, sticky=W)

photo = PhotoImage(file="18x.gif")
Label(root, image=photo).grid(row=0, column=2, rowspan=2, padx=5, pady=5)

Entry(root).grid(row=0, column=1)
Entry(root, show="*").grid(row=1, column=1)

Button(text="upload", width=10).grid(row=2, columnspan=3, pady=5)

mainloop()
