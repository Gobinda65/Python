from tkinter import *
from time import strftime

root = Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S: %p %D')
    label.config(text=string)
    label.after(1000, time)

label = Label(root , font=("ds-digital", 50), background="black", foreground="white")
label.pack(anchor='center')
time()
mainloop()
