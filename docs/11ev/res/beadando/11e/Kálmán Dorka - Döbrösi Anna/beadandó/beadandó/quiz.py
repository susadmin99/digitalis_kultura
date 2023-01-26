#Készítette Kálmán Dorka és Döbrösi Anna 11.e

#ez kell ahhoz hogy lefusson az egész program GUI könyvtár
import tkinter as tk
#functionokat hozzáadjuk a könyvtárból
from tkinter import ttk 

#változó argumentként használjuk a későbbi quiz függvényünkben
y = 0

#egy function ami megvalósítja hogy a kérdések egyesével megjelenjenek, úgy néz ki mint egy notebook, (a) változóba tároljuk
a = ttk.Notebook()

#minden kérdésnek + végének + kezdésnek egy keret, amiben meg fog jelenni az adott szöveg, gomb amit hozzárendelünk
frame0 = ttk.Frame(a)
frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)
frame6 = ttk.Frame(a)

#ablakot csinálunk hogy lássuk magát a programot, paraméter
window = ttk.Frame(a)


#ebben a függvényben tároljuk az összes kérdést és válasz opciókat
def quiz (y):
#add egy függvény ami különböző gombok hozzáadását biztosítja, a gombokét amelyek a lap tetején jelennek meg és ha rányomunk az adott oldalra írt kérdésekhez és válaszokhoz irányít minket, frame1,2.. változók amihez a ttk.Frame-et hozzárendeljük, text szöveg amit ki fog írni a keretek neveként
    a.add(frame0, text ="Kezdés")
    a.add(frame1, text ="Q1")
    a.add(frame2, text ="Q2")
    a.add(frame3, text ="Q3")
    a.add(frame4, text ="Q4" )
    a.add(frame5, text ="Q5")
    a.add(frame6, text ="Vége")

    #a label az egy szövegwidget, a legelső azaz 0 számú keretben fog megjelenni a szöveg, a betűtípus fajtája, mérete, vastagsága, a szöveg elhelyezkedése sor és oszlop alapján
    tk.Label(frame0, text="Biológia ki mit tud", font=("Arial",40, "bold")).grid(row=2, column=2)
    tk.Label(frame0, text="Öt kérdés három válaszlehetőséggel, válaszért szerzett pontok ki lesznek írva, ne feljtse el számolni, hogy egy kis matek kihívás is legyen benne", font =("Arial", 15, "bold")).grid(row=3, column=2)

    #a label az egy szövegwidget, a második azaz 1-es számú keretben fog megjelenni a szöveg, a betűtípus fajtája, mérete, vastagsága, a szöveg elhelyezkedése sor és oszlop alapján
    tk.Label(frame1, text="Melyik a legelterjedtebb poliszacharid?", font=("Arial",40, "bold"),).grid(row=2, column=2)
    #a  button egy gombot jelenít meg az 1-es számú keretben, szöveg, betűtípus, méret, vastagság, a gomb háttérszíne, és a funkciója ami később függvényként van értelmezve, gomb elhelyezkedése sor és oszlop szerint
    tk.Button(frame1, text="Keményítő", font =("Arial",24, "bold"), bg = "light green", command=a1_wrong).grid(row= 3, column=1)
    tk.Button(frame1, text="Glikogén", font =("Arial",24, "bold"), bg = "light blue",command=a1_wrong).grid(row= 3, column=2)
    tk.Button(frame1, text="Cellulóz", font =("Arial",24, "bold"), bg = "light pink",command=a1_correct).grid(row= 3, column=3)

    #a label az egy szövegwidget, a harmadik azaz 2-es számú keretben fog megjelenni a szöveg, a betűtípus fajtája, mérete, vastagsága, a szöveg elhelyezkedése sor és oszlop alapján
    tk.Label(frame2, text="Milyen kötés tartja össze a fehérjéket?", font=("Arial",40, "bold")).grid(row=2, column=2)
    #a  button egy gombot jelenít meg az 2-es számú keretben, szöveg, betűtípus, méret, vastagság, a gomb háttérszíne, és a funkciója ami később függvényként van értelmezve, gomb elhelyezkedése sor és oszlop szerint
    tk.Button(frame2, text="Észter", font =("Arial",24, "bold"), bg = "light green",command=a2_wrong).grid(row= 3, column=1)
    tk.Button(frame2, text="Peptid", font =("Arial",24, "bold"), bg = "light blue",comman=a2_correct).grid(row= 3, column=2)
    tk.Button(frame2, text="Kovalens", font =("Arial",24, "bold"), bg = "light pink",command=a2_wrong).grid(row= 3, column=3)

    #a label az egy szövegwidget, a negyedik azaz 3-as számú keretben fog megjelenni a szöveg, a betűtípus fajtája, mérete, vastagsága, a szöveg elhelyezkedése sor és oszlop alapján
    tk.Label(frame3, text="Melyik az elszappanosítható lipid?", font=("Arial",40, "bold")).grid(row=2, column=2)
    #a  button egy gombot jelenít meg az 3-as számú keretben, szöveg, betűtípus, méret, vastagság, a gomb háttérszíne, és a funkciója ami később függvényként van értelmezve, gomb elhelyezkedése sor és oszlop szerint
    tk.Button(frame3, text="Foszfatid", font =("Arial",24, "bold"), bg = "light green",command=a3_correct).grid(row= 3, column=1)
    tk.Button(frame3, text="Szteroid", font =("Arial",24, "bold"), bg = "light blue",command=a3_wrong).grid(row= 3, column=2)
    tk.Button(frame3, text="Karotinoid", font =("Arial",24, "bold"), bg = "light pink",command=a3_wrong).grid(row= 3, column=3)

    #a label az egy szövegwidget, a ötödik azaz 4-es számú keretben fog megjelenni a szöveg, a betűtípus fajtája, mérete, vastagsága, a szöveg elhelyezkedése sor és oszlop alapján
    tk.Label(frame4, text="Melyik elem építi fel a fogzománcot?", font=("Arial",40, "bold"),).grid(row=2, column=2)
    #a  button egy gombot jelenít meg az 4-es számú keretben, szöveg, betűtípus, méret, vastagság, a gomb háttérszíne, és a funkciója ami később függvényként van értelmezve, gomb elhelyezkedése sor és oszlop szerint
    tk.Button(frame4, text="Fluor", font =("Arial",24, "bold"), bg = "light green", command=a4_correct).grid(row= 3, column=1)
    tk.Button(frame4, text="Nátrium", font =("Arial",24, "bold"), bg = "light blue",command=a4_wrong).grid(row= 3, column=2)
    tk.Button(frame4, text="Magnézium", font =("Arial",24, "bold"), bg = "light pink",command=a4_wrong).grid(row= 3, column=3)

    #a label az egy szövegwidget, a hatodik azaz 5-ös számú keretben fog megjelenni a szöveg, a betűtípus fajtája, mérete, vastagsága, a szöveg elhelyezkedése sor és oszlop alapján
    tk.Label(frame5, text="Hány fokon legsűrűbb a víz?", font=("Arial",40, "bold"),).grid(row=2, column=2)
    #a  button egy gombot jelenít meg az 5-ös számú keretben, szöveg, betűtípus, méret, vastagság, a gomb háttérszíne, és a funkciója ami később függvényként van értelmezve, gomb elhelyezkedése sor és oszlop szerint
    tk.Button(frame5, text="6°", font =("Arial",24, "bold"), bg = "light green", command=a5_wrong).grid(row= 3, column=1)
    tk.Button(frame5, text="10°", font =("Arial",24, "bold"), bg = "light blue",command=a5_wrong).grid(row= 3, column=2)
    tk.Button(frame5, text="4°", font =("Arial",24, "bold"), bg = "light pink",command=a5_correct).grid(row= 3, column=3)

#az a1_correct függvény az első keretben lévő helyes választ meghatározó függvény, annak a parancsa, az egyes keretben megjelenik, hogy a válasz helyes és hogy az elért pont egy, betűtípus, betűméret, betűvastagság, felirat hátterének színe és a felirat színe, elhelyezkedése sor és ozlop szerint
def a1_correct():
    tk.Label(frame1, text="Helyes", font= ("Arial", 24, "bold"), bg = "green", fg = "white").grid(row =1, column= 2)
    tk.Label(frame1, text="Elért pontok:1", font=("Arial,", 20, "bold"), bg="black", fg = "white").grid(row =1, column=3)

#az a1_wrong függvény az első keretben lévő kérdés rossz válaszaira vonatkozó függvény, mely kiírja az egyes keretben, hogy helytelen és pontot nem ért el, betűtípus, betűméret, betűvastagság, felirat hátterének színe és a felirat színe, elhelyezkedése sor és ozlop szerint
def a1_wrong():
    tk.Label(frame1, text="Helytelen", font= ("Arial", 24, "bold"), bg = "red", fg = "white").grid(row =1, column= 2)
    tk.Label(frame1, text="Elért pontok:0", font=("Arial,", 20, "bold"), bg="black", fg = "white").grid(row =1, column=3)

#az a2_correct függvény az első keretben lévő helyes választ meghatározó függvény, annak a parancsa, az egyes keretben megjelenik, hogy a válasz helyes és hogy az elért pont egy, betűtípus, betűméret, betűvastagság, felirat hátterének színe és a felirat színe, elhelyezkedése sor és ozlop szerint
def a2_correct():
    tk.Label(frame2, text="Helyes", font= ("Arial", 24, "bold"), bg = "green", fg = "white").grid(row =1, column= 2)
    tk.Label(frame2, text="Elért pontok:1", font=("Ariel,", 20, "bold"), bg="black", fg = "white").grid(row =1, column=3)

#az a2_wrong függvény az első keretben lévő kérdés rossz válaszaira vonatkozó függvény, mely kiírja az egyes keretben, hogy helytelen és pontot nem ért el, betűtípus, betűméret, betűvastagság, felirat hátterének színe és a felirat színe, elhelyezkedése sor és ozlop szerint
def a2_wrong():
    tk.Label(frame2, text="Helytelen", font= ("Arial", 24, "bold"), bg = "red", fg = "white").grid(row =1, column= 2)
    tk.Label(frame2, text="Elért pontok:0", font=("Arial,", 20, "bold"), bg="black", fg = "white").grid(row =1, column=3)

#az a3_correct függvény az első keretben lévő helyes választ meghatározó függvény, annak a parancsa, az egyes keretben megjelenik, hogy a válasz helyes és hogy az elért pont egy, betűtípus, betűméret, betűvastagság, felirat hátterének színe és a felirat színe, elhelyezkedése sor és ozlop szerint
def a3_correct():
    tk.Label(frame3, text="Helyes", font= ("Arial", 24, "bold"), bg = "green", fg = "white").grid(row =1, column= 2)
    tk.Label(frame3, text="Elért pontok:1", font=("Arial,", 20, "bold"), bg="black", fg = "white").grid(row =1, column=3)

#az a3_wrong függvény az első keretben lévő kérdés rossz válaszaira vonatkozó függvény, mely kiírja az egyes keretben, hogy helytelen és pontot nem ért el, betűtípus, betűméret, betűvastagság, felirat hátterének színe és a felirat színe, elhelyezkedése sor és ozlop szerint
def a3_wrong():
    tk.Label(frame3, text="Helytelen", font= ("Arial", 24, "bold"), bg = "red", fg = "white").grid(row =1, column= 2)
    tk.Label(frame3, text="Elért pontok:0", font=("Arial,", 20, "bold"), bg="black", fg = "white").grid(row =1, column=3)

#az a4_correct függvény az első keretben lévő helyes választ meghatározó függvény, annak a parancsa, az egyes keretben megjelenik, hogy a válasz helyes és hogy az elért pont egy, betűtípus, betűméret, betűvastagság, felirat hátterének színe és a felirat színe, elhelyezkedése sor és ozlop szerint
def a4_correct():
    tk.Label(frame4, text="Helyes", font= ("Arial", 24, "bold"), bg = "green", fg = "white").grid(row =1, column= 2)
    tk.Label(frame4, text="Elért pontok:1", font=("Arial,", 20, "bold"), bg="black", fg = "white").grid(row =1, column=3)

#az a4_wrong függvény az első keretben lévő kérdés rossz válaszaira vonatkozó függvény, mely kiírja az egyes keretben, hogy helytelen és pontot nem ért el, betűtípus, betűméret, betűvastagság, felirat hátterének színe és a felirat színe, elhelyezkedése sor és ozlop szerint
def a4_wrong():
    tk.Label(frame4, text="Helytelen", font= ("Arial", 24, "bold"), bg = "red", fg = "white").grid(row =1, column= 2)
    tk.Label(frame4, text="Elért pontok:0", font=("Arial,", 20, "bold"), bg="black", fg = "white").grid(row =1, column=3)

#az a5_correct függvény az első keretben lévő helyes választ meghatározó függvény, annak a parancsa, az egyes keretben megjelenik, hogy a válasz helyes és hogy az elért pont egy, betűtípus, betűméret, betűvastagság, felirat hátterének színe és a felirat színe, elhelyezkedése sor és ozlop szerint
def a5_correct():
    tk.Label(frame5, text="Helyes", font= ("Arial", 24, "bold"), bg = "green", fg = "white").grid(row =1, column= 2)
    tk.Label(frame5, text="Elért pontok:1", font=("Ariel,", 20, "bold"), bg="black", fg = "white").grid(row =1, column=3)

#az a5_wrong függvény az első keretben lévő kérdés rossz válaszaira vonatkozó függvény, mely kiírja az egyes keretben, hogy helytelen és pontot nem ért el, betűtípus, betűméret, betűvastagság, felirat hátterének színe és a felirat színe, elhelyezkedése sor és ozlop szerint#az a1_wrong függvény az első keretben lévő kérdés rossz válaszaira vonatkozó funkció, mely kiírja az egyes keretben, hogy helytelen és pontot nem ért el, betűtípus, betűméret, betűvastagság, felirat hátterének színe és a felirat színe, elhelyezkedése sor és ozlop szerint
def a5_wrong():
    tk.Label(frame5, text="Helytelen", font= ("Arial", 24, "bold"), bg = "red", fg = "white").grid(row =1, column= 2)
    tk.Label(frame5, text="Elért pontok:0", font=("Arial,", 20, "bold"), bg="black", fg = "white").grid(row =1, column=3)

#az utolsó, hatos számú keretben megjelenik a szövegwidget, betűtípus, betűméret, betűvastagság, sor és oszlop alapján elhelyezve
tk.Label(frame6, text="Köszönjük, hogy játszott!:)", font=("Arial",40, "bold")).grid(row=3, column=2)
#hatos számú keretben megjelenő gomb, kilépés felirattal, betűtípus, betűméret, betűvastagság, háttérszíne a gombnak, felirat színe a gombon, kilépés paranccsal, tehét bezárja a programot, sor és oszlop szerint elhelyezve
tk.Button(frame6, text = "Kilépés", font = ("Arial", 24, "bold" ), bg = "light pink" , fg = "black", command=quit).grid(row =2, column=3)

#meghívjuk a függvényt
quiz(y)
#becsomagoljuk az egész programot hogy megjelenjen az ablakban
a.pack()
#utolsó sor amivel lezárjuk a programot
window.mainloop()

