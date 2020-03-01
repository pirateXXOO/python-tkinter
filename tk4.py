from tkinter import *

root = Tk()

photo = PhotoImage(file='18x.gif')
theLabel = Label(root,
                 text='Xiaomai\nSaigao',
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 fg='red')
theLabel.pack()

mainloop()