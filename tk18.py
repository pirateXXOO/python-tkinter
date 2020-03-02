from tkinter import *

master = Tk()

theLB = Listbox(master, selectmode=EXTENDED)
theLB.pack()

# theLB.insert(0, "You are pig")
# theLB.insert(END, "He is pig")

for item in ["Egg", "Watermelon", "Chicken", "meat"]:
    theLB.insert(END, item)


theButton = Button(master, text="Delete it.", command=lambda x=theLB: x.delete(ACTIVE))
theButton.pack()

mainloop()
