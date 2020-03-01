import tkinter as tk

app = tk.Tk()
app.title('Tkinter Demo')

theLabel = tk.Label(app, text='My fist GUI program. ')
theLabel.pack()

app.mainloop()