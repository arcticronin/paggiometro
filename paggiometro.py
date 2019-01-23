from tkinter import *
from backend import *
from tk_tools import *

window=Tk()

led1 = Led(window, size=50)
led1.grid(row=0,column=0,pady=(20,10))
led1.to_grey()

paggezza_text=StringVar()
e1=Entry(window,textvariable=paggezza_text)
e1.grid(row=0,column=1,padx=(20,10))


gauge= Gauge(window, max_value=100.0, label='Paggezza', unit='pg',
            height=150, width=250,divisions=20,yellow=30,bg=None)
gauge.grid(row=1,column=0,columnspan=2)
gauge.set_value(70)


l2=Label(window, text="V  Inserisci Nome  V")
l2.grid(row=2,column=0, columnspan=2, pady=(15,10))

ricerca=StringVar()
e2=Entry(window,textvariable=ricerca)
e2.grid(row=3,column=0, columnspan=2)

b1=Button(window,text="Calcola Paggezza",width=20,font=("monospace",15,"bold"))
b1.grid(row=4,column=0,columnspan=2, pady=15, padx=10)



window.mainloop()
