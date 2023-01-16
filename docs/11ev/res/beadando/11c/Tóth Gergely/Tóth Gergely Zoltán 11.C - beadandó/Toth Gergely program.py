#Beimportálom a kellő dolgokat
import tkinter as tk
import random
import string
import math
from tkinter import messagebox

#Létrehozom a jelszó generátort
def passwordGenerator():
    #Létrehozom a mennyiség számolónak a + és - funkcióját
    def increase():
        value = int(valueLabel["text"])
        valueLabel["text"] = f"{value + 1}"

    def decrease():
        value = int(valueLabel["text"])
        valueLabel["text"] = f"{value - 1}"

    #Létrehozom a "mehet" funkciót, amely megnézi, hogy hány karakter hosszú legyen a jelszó, és ha 0 vagy kevesebb a szám egy errort dob be    
    def Calc():
        if int(valueLabel["text"]) <= 0:
            messagebox.showerror("Error", "Nem lehet a szám 0 vagy minusz")
        else:
            entry.delete(0,'end')
            characters = string.ascii_letters + string.digits + string.punctuation
            characters = characters.replace(" ", random.choice(characters))
            password = ''.join(random.choice(characters) for i in range(int(valueLabel["text"])))
            entry.insert(0, password)

    #Létrehozom a másolási funkciót
    def copyText():
        entry.select_range(0,'end')
        entry.event_generate("<<Copy>>")

    #Létrehozom az ablakot
    window = tk.Tk()
    window.title("Jelszó generátor")
    window.resizable(width=False, height=False)

    frame = tk.Frame(master=window, width=250, height=350)
    frame.pack()

    #Létrehozom a szövegeket, majd elhelyezem őket progrtamban
    label1 = tk.Label(master=frame, text="Jelszó generátor")
    label1.place(x=125, y=20, anchor=tk.CENTER)

    label2 = tk.Label(master=frame, text="Karakterek száma:")
    label2.place(x=0, y=60)

    valueLabel = tk.Label(master=window, text="0")
    valueLabel.place(x=125, y=70, anchor=tk.CENTER)

    #Létrehozom az emelkedés és csökkenés gombokat
    decreaseButton = tk.Button(master=window, text="-", command=decrease, width=2, height=1)
    decreaseButton.place(x=90, y=90)

    increaseButton = tk.Button(master=window, text="+", command=increase, width=2, height=1)
    increaseButton.place(x=135, y=90)


    
    #Létrehozom a "mehet" gombot, ami össze van kötve a Calc funkcióval
    goButton = tk.Button(master=window, text="Mehet", width=5, height=1, command=Calc)
    goButton.place(x=125, y=140, anchor=tk.CENTER)

    #Létehozok egy dobozt, amibe a jelszó fog kerülni
    entry = tk.Entry(master=window)
    entry.place(x=125, y=170, anchor=tk.CENTER)

    #Létrehozom a másolás gombot
    copyButton = tk.Button(master=window, text="Másolás", command=copyText)
    copyButton.place(x=125, y=200, anchor=tk.CENTER)

    #Bezárom a menüt
    menu.destroy()

    #"Loopolom" a "window" nevű ablakot
    window.mainloop()




#Létrehozom a kamat kalkulátort
def kamatCalculator():

    #Létrehozok egy funkciót, ami a "klabel7"-nek állítja be a szövegét kiválasztásra
    def period(frequency):

        if frequency == "halfyear":
            kLabel7.config(text="félév")
        elif frequency == "month":
            kLabel7.config(text="hónap")
        elif frequency == "year":
            kLabel7.config(text="év")

    #Létrehozom az ablakot, ami a kamat kalkulátor névre hallgat
    calculator = tk.Tk()
    calculator.title("Kamat kalkulátor")
    calculator.resizable(width=False, height=False)

    #Létrehozok kettő változót
    var= tk.IntVar(master=calculator)
    var2 = tk.StringVar(master=calculator)

    calcFrame = tk.Frame(master=calculator, width=250, height=450)
    calcFrame.pack()

    #Létrehozom a szövegeket
    kLabel1 = tk.Label(master=calcFrame, text="Kamat kalkulátor")
    kLabel1.place(x=125, y=20, anchor=tk.CENTER)

    kLabel2 = tk.Label(master=calcFrame, text="Milyen kamatot szeretne?")
    kLabel2.place(x=10, y=40)

    #Lérehozom a választó gombokat
    kRadio1 = tk.Radiobutton(master=calcFrame, text="Egyszerű kamat", variable=var, value=1)
    kRadio1.place(x=10, y=60)

    kRadio2 = tk.Radiobutton(master=calcFrame, text="Kamatos kamat", variable=var, value=2)
    kRadio2.place(x=10, y=80)

    #Kiválasztom a "kRadio1" gombot
    kRadio1.select()

    #Létrehozok további szövegeket
    kLabel3 = tk.Label(master=calcFrame, text="Milyen időszakonként kamatozódjon?")
    kLabel3.place(x=10, y=100)

    kLabel7 = tk.Label(master=calcFrame, text="félév")
    kLabel7.place(x=130,y=238)

    #Létrehozok további gombokat
    kRadio3 = tk.Radiobutton(master=calcFrame, text="Félévente", variable=var2, value="halfyear", command=lambda: period(var2.get()))
    kRadio3.place(x=10, y=120)


    kRadio4 = tk.Radiobutton(master=calcFrame, text="Évente", variable=var2, value="year", command=lambda: period(var2.get()))
    kRadio4.place(x=10, y=140)

    kRadio5 = tk.Radiobutton(master=calcFrame, text="Havonta", variable=var2, value="month", command=lambda: period(var2.get()))
    kRadio5.place(x=10, y=160)

    #Kiválasztom a "kRadio3" gombot
    kRadio3.select()

    #Létrehozok még szövegeket és bemeneteli ablakokat
    kLabel4 = tk.Label(master=calcFrame, text="Mennyit szeretne felvenni?")
    kLabel4.place(x=10, y=180)

    kEntry1 = tk.Entry(master=calcFrame)
    kEntry1.place(x=10, y=200)

    kLabel5 = tk.Label(master=calcFrame, text="Ft")
    kLabel5.place(x=130, y=198)

    kLabel6 = tk.Label(master=calcFrame, text="Mennyi időre szeretné felvenni?")
    kLabel6.place(x=10,y=220)

    kEntry2 = tk.Entry(master=calcFrame)
    kEntry2.place(x=10, y=240)

    kLabel8 = tk.Label(master=calcFrame, text="Mennyi az éves kamat?")
    kLabel8.place(x=10, y=260)

    kEntry3 = tk.Entry(master=calcFrame)
    kEntry3.place(x=10, y=280)

    kLabel9 = tk.Label(master=calcFrame, text="%")
    kLabel9.place(x=130, y=278)

    kEntry4 = tk.Entry(master=calcFrame)
    kEntry4.place(x=10, y=340)

    kLabel10 = tk.Label(master=calcFrame, text="Ft")
    kLabel10.place(x=130, y=338)

    #Létrehozom a kalkulálási funkciót, amely kiszámolja nekem a kiválasztott kamatot
    def calculation(var1, var2, money, duration, kamat):

        #Megnézem, hogy nem üres-e valamelyi rublika
        if kEntry1.index("end") == 0 or kEntry2.index("end") == 0 or kEntry3.index("end") == 0:
            messagebox.showerror("Error", "Hiányosak az adatok, kérem töltse ki az egészet")
            return

        money = float(money)
        duration = float(duration)
        kamat = (float(kamat) / 100)

        #Kitörlöm a szöveget, ami a "kEntry4"-ben van
        kEntry4.delete(0,'end')

        if var1 == 1:
            if var2 == "year":
                result = (money*(1+kamat*duration))
                kEntry4.insert(0, result)
            elif var2 == "month":
                result = (money*(1+kamat*duration))
                kEntry4.insert(0, result)
            elif var2 == "halfyear":
                result = (money*(1+kamat*duration))
                kEntry4.insert(0, result)
        elif var1 == 2:
            if var2 == "year":
                result = (money*(math.pow((1+kamat), duration)))
                kEntry4.insert(0, result)
            elif var2 == "month":
                kam = (kamat)/12
                dur = (duration) * 12
                result = (money*(math.pow((1+kam), dur)))
                kEntry4.insert(0, result)
            elif var2 == "halfyear":
                kam = (kamat)/2
                dur = (duration) * 2
                result = (money*(math.pow((1+kam), dur)))
                kEntry4.insert(0, result)


    #Létrehozom a "mehet" gombot, ami elindítja a "calculation" funkciót
    kButton = tk.Button(master=calcFrame, text="Mehet", width=5, height=1, command=lambda: calculation(var1=var.get(), var2=var2.get(), money=kEntry1.get(), duration=kEntry2.get(), kamat=kEntry3.get()))
    kButton.place(x=125, y=320, anchor=tk.CENTER)

    #Bezárom a "menu" ablakot
    menu.destroy()
    #"Loopolom" a "calculator" nevű ablakot
    calculator.mainloop()

#Létrehozom a menüt
menu = tk.Tk()
menu.title("Menü")
menu.resizable(width=False, height=False)

mFrame = tk.Frame(master=menu, width=400, height=200)
mFrame.pack()

#Létrehozom a szöveget
menuLabel = tk.Label(master=mFrame, text="Válasszon egyet az alábbiak közül:")
menuLabel.place(x=200, y=20, anchor=tk.CENTER)


#Létrehozom a gombokat
menuButton1 = tk.Button(master=menu, text="Jelszó generátor", width=15, height=9, command=passwordGenerator)
menuButton1.place(x=10, y=50)

menuButton2 = tk.Button(master=menu, text="Kamat kalkulátor", width=15, height=9, command=kamatCalculator)
menuButton2.place(x=275, y=50)

#"Loopolom" a "menu" nevű ablakot
menu.mainloop()