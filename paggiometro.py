from tkinter import *
from . import backend.py

window=Tk()

l1=Label(window, text="PaggioMetro")
l1.grid(row=0,column=0)

l2=Label(window, text="V-Inserisci Nome-V")
l2.grid(row=1,column=0)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=2,column=0)

b1=Button(window,text="Calcola",width=12)
b1.grid(row=3,column=0)

title_text=StringVar()
e2=Entry(window,textvariable=title_text2)
e2.grid(row=4,column=0)



window.mainloop()
