from tkinter import *

root = Tk()


def callback():
    var.set("No, You haven't!")


frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('Warning ! \nThe content you downloaded is not suitable for people under the age of 18')

textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='./18x.gif')
imgLabel = Label(frame1, image=photo )
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text='I have been 18 years older.', command=callback)
theButton.pack()

frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)


mainloop()