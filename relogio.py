'''
# Relógio Digital : Python
# Renato Sanches : WebMundi.com | XP IT Tecnologia
# Informações / Code : https://bit.ly/python-tip
'''

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Relógio Digital Python : WebMundi.com : XP IT Tecnologia")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("ds-digital", 80), background = "black", foreground = "#ffd60a")
label.pack(anchor = 'center')
time()

mainloop()