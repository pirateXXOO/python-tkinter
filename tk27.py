from tkinter import *
import webbrowser

root = Tk()

text = Text(root, width=30, height=5)
text.pack()

text.insert(INSERT, "I love you. ")

text.tag_add("link", "1.7", "1.10")
text.tag_config("link", foreground="blue", underline=True)


def show_hand_cursor(event):
    text.config(cursor="arrow")


def show_xterm_cursor(event):
    text.config(cursor="xterm")


def click(event):
    webbrowser.open("https://www.baidu.com")


text.tag_bind("link", "<Enter>", show_hand_cursor)
text.tag_bind("link", "<Leave>", show_xterm_cursor)
text.tag_bind("link", "<Button-1>", click)

mainloop()
