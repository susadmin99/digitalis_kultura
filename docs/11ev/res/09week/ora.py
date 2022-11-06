#Ez elég fontos dolog, enélkül nem működik semmi
import tkinter as tk

#Kell egy window vagy valami ami egyenlő a TK()-val, hogy lássunk is valamit
window = tk.Tk()

hello = tk.Label(text="Hello, Tkinter")

hello.pack()

#Label - Egyszerű szöveg widget
szoveg1 = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)

#Button - Gomb widget
gomb = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

bemenet_szoveg = tk.Label(text="Name")

#Entry - Bemeneti widget
bemenet = tk.Entry()

nev = bemenet.get()
print(nev)

szoveg_doboz = tk.Text()

#mindent is csomagolunk
szoveg_doboz.pack()
bemenet_szoveg.pack()
bemenet.pack()
gomb.pack()
szoveg1.pack()
hello.pack()

#a mainloop mindig a legutolsó sor legyen a fájlban
window.mainloop()