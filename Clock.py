from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

def time():                                                     #Função que nos irá mostrar o tempo na label
    string = strftime('%H:%M:%S  %p')
    label.config(text=string)
    label.after(1000, time)  #a cada segundo chama a função




label = Label(root, font=("ds-digital", 80), background = "black", foreground = "red") #Visual da Label (janel onde nos apresentará as horas
label.pack(anchor="center")
time()

mainloop()
