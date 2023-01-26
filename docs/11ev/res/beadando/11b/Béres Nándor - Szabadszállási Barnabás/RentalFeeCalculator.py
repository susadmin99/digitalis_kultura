# Az ablak megtervezése
import tkinter as tk

window = tk.Tk()
window.geometry("1000x700")
window.title("Rental Fee Calculator")

# 1.doboz neve és funkciója
alabel = tk.Label(window, text="Felvett kölcsön összege (Ft)")
alabel.pack()
asv = tk.StringVar()
asv.trace("w", lambda name, index, mode, asv=asv: asvcallback(asv))
a = tk.Entry(window, textvariable=asv)
a.pack()
# 2.doboz neve és funkciója
blabel = tk.Label(window, text="Teljes hiteldíj mutató (%)")
blabel.pack()
bsv = tk.StringVar()
bsv.trace("w", lambda name, index, mode, bsv=bsv: bsvcallback(bsv))
b = tk.Entry(window, textvariable=bsv)
b.pack()
# 3.doboz neve és funkciója
clabel = tk.Label(window, text="Visszafizetés ideje hónapban")
clabel.pack()
csv = tk.StringVar()
csv.trace("w", lambda name, index, mode, csv=csv: csvcallback(csv))
c = tk.Entry(window, textvariable=csv)
c.pack()
# 4.doboz neve és funkciója
dlabel = tk.Label(window, text="Kívánt havi profit (%)")
dlabel.pack()
dsv = tk.StringVar()
dsv.trace("w", lambda name, index, mode, dsv=dsv: dsvcallback(dsv))
d = tk.Entry(window, textvariable=dsv)
d.pack()
# 5.doboz neve és funkciója
elabel = tk.Label(window, text="Havi átlagos kiadások összege (Ft)")
elabel.pack()
esv = tk.StringVar()
esv.trace("w", lambda name, index, mode, esv=esv: esvcallback(esv))
e = tk.Entry(window, textvariable=esv)
e.pack()
# A dobozokban megadható karakterek értéke + ha nem szám = piros a doboz
flag= ["n","n","n","n","n"]

def asvcallback(var):
    try:
        int(var.get())
    except:
        a.config({"background": "Red"})
        flag[0] = "1"
    else:
        a.config({"background": "White"})
        flag[0] = "n"
    finally:
        button_switch()

def bsvcallback(var):
    try:
        int(var.get())
    except:
        b.config({"background": "Red"})
        flag[1] = "1"
    else:
        b.config({"background": "White"})
        flag[1] = "n"
    finally:
        button_switch()

def csvcallback(var):
    try:
        int(var.get())
    except:
        c.config({"background": "Red"})
        flag[2] = "1"
    else:
        c.config({"background": "White"})
        flag[2] = "n"
    finally:
        button_switch()

def dsvcallback(var):
    try:
        int(var.get())
    except:
        d.config({"background": "Red"})
        flag[3] = "1"
    else:
        d.config({"background": "White"})
        flag[3] = "n"
    finally:
        button_switch()

def esvcallback(var):
    try:
        int(var.get())
    except:
        e.config({"background": "Red"})
        flag[4] = "1"
    else:
        e.config({"background": "White"})
        flag[4] = "n"
    finally:
        button_switch()
# Számolás + eredmény
def szamolas():
    a1 = int(a.get())
    b1 = int(b.get()) /100 + 1
    c1 = int(c.get())
    d1 = int(d.get()) /100
    e1 = int(e.get())
    havifizetnivalo = a1 * b1 / c1 + e1
    eredmeny = havifizetnivalo * (1 + d1 )
    label.config(text=int(round(eredmeny, 0)))
# Gomb + funkció
button = tk.Button(window,text='Számolás', command=szamolas)
button.pack()

label2 = tk.Label(window, text="Ennyi bért kéne kérni, hogy kért % legyen a profit")
label2.pack()
# Gomb mikor aktiválható
def button_switch():
    if "1" in flag:
        button.config(state= "disabled")
    else:
        button.config(state= "active")

label = tk.Label(window)
label.pack()

window.mainloop()