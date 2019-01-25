from tkinter import *
import backend
from tk_tools import *


def esegui():
    nome = paggezza_text.get()
    pgg = backend.ricerca(nome)
    gauge.set_value(pgg)
    if (pgg < 30):
        led1.to_green
    elif (pgg < 50):
        led1.to_yellow
    else:
        led1.to_red


window = Tk()

led1 = Led(window, size=50)
led1.grid(row=0, column=0, pady=(20, 10))
led1.to_grey()

paggezza_num = StringVar()
e1 = Entry(window, textvariable=paggezza_num)
e1.grid(row=0, column=1, padx=(20, 10))


gauge = Gauge(window, max_value=100.0, label='Paggezza', unit='pg',
              height=150, width=250, divisions=20, yellow=30, bg=None)
gauge.grid(row=1, column=0, columnspan=2)

l2 = Label(window, text='V  Inserisci Nome  V')
l2.grid(row=2, column=0, columnspan=2, pady=(15, 10))

paggezza_text = StringVar()
e2 = Entry(window, textvariable=paggezza_text)
e2.grid(row=3, column=0, columnspan=2)

b1 = Button(window, text='Calcola Paggezza', width=20, command=esegui,
            font=("monospace", 15, "bold"))
b1.grid(row=4, column=0, columnspan=2, pady=15, padx=10)

gauge.set_value(96)
led1.to_red()


def ricerca(nome):
    conn = backend.sqlite3.connect("paggi.db")
    cur = conn.cursor()
    nome = paggezza_text.get()
    # cheat VVV
    lu = 'luca'
    cur.execute("SELECT pag FROM paggio WHERE nome = ? ", lu)
    num = int(cur.fetchone())
    conn.close()
    if (num == ""):
        return random.randint(0, 100)
    return num


uno = ricerca('luca')

print(uno)

window.mainloop()
