
import tkinter as tk

#Az elemek létrehozása

ablak = tk.Tk()
ablak.title("Hány év múlva leszek 100?")

felirat1 = tk.Label(ablak, text="Add meg az életkorod!")
felirat1.pack()

felirat2 = tk.Entry(ablak)
felirat2.pack()

eredmény = tk.Label(ablak)
eredmény.pack()

#A bekért kor alapján kiszámolja hány év múlva leszel 100, ha elmúltál már akkor azt írja ki

def számolás():
    jelenlegi_kor = int(felirat2.get())
    kiszámolt_kor = 100 - jelenlegi_kor
    if jelenlegi_kor > 100:
        eredmény.config(text=f'Elmúltál már 100 éves :D')
    else:
        eredmény.config(text=f'100 éves leszel {kiszámolt_kor} év múlva.')

#A kiszámolás gomb elindítja a számolás függvényt

kiszámolás_gomb = tk.Button(ablak, text="Kiszámolás", command = számolás)
kiszámolás_gomb.pack()

ablak.mainloop()