from tkinter import *

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "I love you. ")

text.tag_add("tag1", "1.7", "1.10", "1.11")
text.tag_add("tag2", "1.7", "1.10", "1.11")
text.tag_config("tag1", background="yellow", foreground="blue")

text.tag_config("tag2", background="red")

mainloop()
