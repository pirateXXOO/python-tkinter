from tkinter import *

root = Tk()

textLabel = Label(root, text='Warning ! \nThe content you downloaded is not suitable for people under the age of 18',
                  justify=LEFT,
                  padx=10)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='./18x.gif')
imgLabel = Label(root, image=photo )
imgLabel.pack(side=RIGHT)

mainloop()