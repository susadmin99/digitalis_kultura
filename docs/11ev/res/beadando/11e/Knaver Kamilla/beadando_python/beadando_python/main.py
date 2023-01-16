import tkinter as tk
from tkinter import ttk


root = tk.Tk()
# program címének beállítása
root.title('Pizza Queen')

# program ikonjának beállítása
photo = tk.PhotoImage(file='pizza.png')
root.wm_iconphoto(False, photo)

# alkalmazás felbontásának beállítása
root.geometry('900x600')

# globális változók létrehozása
clicked = tk.StringVar()
okStreet = 0
priceInCart = 0

street = tk.StringVar
floor = tk.IntVar
houseNum = tk.IntVar
postalCode = tk.IntVar
phoneNum = tk.IntVar

# első oldal
def tab1():
    # második oldal
    def tab2():
        # harmadik oldal
        def tab3():
            # feltétel a továbblépéshez, hogy legyen rendelés
            listSize = listBasket.size()
            if listSize != 0:
                buttonBackToMain.destroy()
                pizzasAndBasketFrame.destroy()
                price.destroy()
                buttonSubOrder.destroy()

                # globális változók használata
                global floor
                global postalCode
                global street
                global phoneNum
                global houseNum

                # a kisszállítási címet kiírása
                delivery = tk.Label(root, text="The delivery has been started to ...", font=('Arial', 20))
                delivery.pack(padx=20, pady=60)

                # ha a felhasználó adott meg emelet számot, az esetben máshogy írja ki a címet
                if str(floor) == "":
                    delivery.config(
                        text=f"The delivery has been started to {str(postalCode)}, {str(houseNum)}, {str(street)} Street.")
                else:
                    delivery.config(
                        text=f"The delivery has been started to {str(postalCode)}, {str(houseNum)}, {str(street)} Street, Floor: {str(floor)}.")

                # várható időtartam szöveg kiírása (csak szöveg)
                estTime = tk.Label(root, text="Estimated time: 30 minutes", font=('Arial', 20))
                estTime.pack(padx=20, pady=20)

            else:
                tab2()

        # globális változók használata
        global floor
        global postalCode
        global street
        global phoneNum
        global houseNum

        # értékek globális változókhoz való hozzárendelése
        houseNum = inputHouseNum.get("1.0", "end-1c")
        phoneNum = inputPhoneNum.get("1.0", "end-1c")
        street = inputStreet.get("1.0", "end-1c")
        floor = inputFloorNum.get("1.0", "end-1c")
        postalCode = comboboxPostalCode.get()

        # ellenőrzés, hogy a megadott utca neve típuskényszeríthető-e int-é
        def try_parse_int(inStreet):
            global okStreet
            try:
                return int(inStreet)
            except:
                return None

        try_parse_int(street)
        # abban az esetben, ha sikerült a típuskényszerítés
        if street.isnumeric():
            return None
        else:
            okStreet = 1

        # ha a felhasználó helytelen értékeked ad meg, nem enged tovább a program
        if houseNum.isnumeric() and phoneNum.isnumeric() and okStreet == 1 and postalCode.isnumeric():
            welcomeT.destroy()
            addressFrame.destroy()
            buttonSubmit.destroy()

            # visszalépő gomb metódusa, amit a gombra kattintva vissza lépteti a felhasznlót a cím megadása oldalra(tab1)
            def back():
                buttonBackToMain.destroy()
                pizzasAndBasketFrame.destroy()
                price.destroy()
                buttonSubOrder.destroy()
                tab1()

            # kosár űrítése gomb metódusa, amit a gombra kattintva kiűríti a kosarat
            def resetBasket():
                global priceInCart
                priceInCart = 0
                price.config(text=f"Price: {str(priceInCart)} Ft")
                listBasket.delete(0, tk.END)

            # egy húsimádó pizzát ad a kosárhoz és megnöveli a fizetendő összeget az adott pizza árával, valamint kiíratja az új "priceInCart" értéket
            def addMeatPizza():
                listBasket.insert("end", 'Meat Lover Pizza  -  2700 Ft')
                global priceInCart
                priceInCart += 2700
                price.config(text=f"Price: {str(priceInCart)} Ft")

            # egy négysajtos pizzát ad a kosárhoz és megnöveli a fizetendő összeget az adott pizza árával, valamint kiíratja az új "priceInCart" értéket
            def addCheesePizza():
                listBasket.insert("end", 'Four Cheeese Pizza  -  2800 Ft')
                global priceInCart
                priceInCart += 2800
                price.config(text=f"Price: {str(priceInCart)} Ft")

            # egy sonkás gombás pizzát ad a kosárhoz és megnöveli a fizetendő összeget az adott pizza árával, valamint kiíratja az új "priceInCart" értéket
            def addMHAndHamPizza():
                listBasket.insert("end", 'Ham and Mushroom Pizza  -  3000 Ft')
                global priceInCart
                priceInCart += 3000
                price.config(text=f"Price: {str(priceInCart)} Ft")

            # egy BBQ pizzát ad a kosárhoz és megnöveli a fizetendő összeget az adott pizza árával, valamint kiíratja az új "priceInCart" értéket
            def addBBQPizza():
                listBasket.insert("end", 'BBQ Pizza  -  2850 Ft')
                global priceInCart
                priceInCart += 2850
                price.config(text=f"Price: {str(priceInCart)} Ft")

            # keret létrehozása, esztétikai elem
            pizzasAndBasketFrame = tk.Frame(root)

            # keret oszlopkonfigurációja
            pizzasAndBasketFrame.columnconfigure(0, weight=1)
            pizzasAndBasketFrame.columnconfigure(1, weight=1)
            pizzasAndBasketFrame.columnconfigure(2, weight=1)
            pizzasAndBasketFrame.columnconfigure(3, weight=1)

            # pizzák felirat létrehozása és keretbe rendezése, megjelenítése
            BasketT = tk.Label(pizzasAndBasketFrame, text="Pizzas", font=('Arial', 20))
            BasketT.grid(row=0, column=0, sticky=tk.E + tk.W, padx=20, pady=20)

            # húsimádó pizza felirat létrehozása
            pizzaMeat = tk.Label(pizzasAndBasketFrame, text="Meat Lover Pizza", font=('Arial', 16))
            pizzaMeat.grid(row=1, column=0, sticky=tk.E + tk.W, padx=5, pady=20)
            #gomb, amely húsimádó pizzát ad a kosárba
            buttonPizzaMeat = tk.Button(pizzasAndBasketFrame, text="Add", height=1, width=7, font=('Arial', 16), bg="green", fg="white", command=addMeatPizza)
            buttonPizzaMeat.grid(row=1, column=1, sticky=tk.E + tk.W, padx=5, pady=20)

            #sonkás gombás pizza felirat létrehozása
            pizzaMRHam = tk.Label(pizzasAndBasketFrame, text="Ham and Mushroom Pizza", font=('Arial', 16))
            pizzaMRHam.grid(row=2, column=0, sticky=tk.E + tk.W, padx=5, pady=0)
            #gomb, amely sonkás gombás pizzát ad a kosárba
            buttonPizzaMRHam = tk.Button(pizzasAndBasketFrame, text="Add", height=1, width=7, font=('Arial', 16), bg="green", fg="white", command=addMHAndHamPizza)
            buttonPizzaMRHam.grid(row=2, column=1, sticky=tk.E + tk.W, padx=5, pady=0)

            #BBQ pizza felirat létrehozása
            pizzaBBQ = tk.Label(pizzasAndBasketFrame, text="BBQ Pizza", font=('Arial', 16))
            pizzaBBQ.grid(row=3, column=0, sticky=tk.E + tk.W, padx=5, pady=20)
            #gomb, amely BBQ pizzát ad a kosárba
            buttonPizzaBBQ = tk.Button(pizzasAndBasketFrame, text="Add", height=1, width=7, font=('Arial', 16), bg="green", fg="white", command=addBBQPizza)
            buttonPizzaBBQ.grid(row=3, column=1, sticky=tk.E + tk.W, padx=5, pady=20)

            #négysajtos pizza felirat létrehozása
            pizzaCheese = tk.Label(pizzasAndBasketFrame, text="Four Cheeses Pizza", font=('Arial', 16))
            pizzaCheese.grid(row=4, column=0, sticky=tk.E + tk.W, padx=5, pady=0)
            #gomb, amely négysajtos pizzát ad a kosárba
            buttonPizzaCheese = tk.Button(pizzasAndBasketFrame, text="Add", height=1, width=7, font=('Arial', 16), bg="green", fg="white", command=addCheesePizza)
            buttonPizzaCheese.grid(row=4, column=1, sticky=tk.E + tk.W, padx=5, pady=0)

            # kosár felirat létrehozása és keretbe rendezése, megjelenítése
            BasketT = tk.Label(pizzasAndBasketFrame, text="Cart", font=('Arial', 20))
            BasketT.grid(row=0, column=2, sticky=tk.E + tk.W, padx=40, pady=20)

            # kosár létrehozása listbox-al
            listBasket = tk.Listbox(pizzasAndBasketFrame, width=35, height=15, bg="skyblue4", font=22, foreground="white")
            listBasket.grid(row=1, column=2, sticky=tk.E + tk.W, padx=40, pady=20, rowspan=30)

            # kosár űrítése gomb létrehozása
            buttonResetBasket = tk.Button(pizzasAndBasketFrame, text="Clear Cart", height=1, width=7, font=('Arial', 16), bg="red4", fg="white", command=resetBasket)
            buttonResetBasket.grid(row=11, column=2, sticky=tk.E + tk.W, padx=40, pady=20)

            # keret megjelenítése
            pizzasAndBasketFrame.pack()

            # fizetendő végösszeg felirat létrehozása
            price = tk.Label(root, text="Price: 0 Ft", font=('Arial', 20))
            # fizetendő végösszeg felirat megjelenítése
            price.pack(padx=20, pady=20)

            # rendelés leadása gomb létrehozása és megjelenítése
            buttonSubOrder = tk.Button(root, text="Submit Order", height=1, width=12, font=('Arial', 16), bg="green", fg="white", command=tab3)
            buttonSubOrder.pack(padx=20, pady=0)

            # a vissza gomb létrehozása és megjelenítése
            buttonBackToMain = tk.Button(root, text="Back", height=1, width=7, font=('Arial', 16), bg="red4", fg="white", command=back)
            buttonBackToMain.pack(padx=20, pady=20, side='bottom')
        else:
            #tab1 elemeinek eltüntetése
            welcomeT.destroy()
            addressFrame.destroy()
            buttonSubmit.destroy()
            tab1()

    # üdvözlőszöveg létrehozása és kiírása
    welcomeT = tk.Label(root, text="Welcome to Pizza Queen!", font=('Arial', 20))
    welcomeT.pack(padx=20, pady=60)

    # keret létrehozása
    addressFrame = tk.Frame(root)
    addressFrame.columnconfigure(0, weight=1)
    addressFrame.columnconfigure(1, weight=1)

    # "Address" szöveg létrehozása, keretbe rendezése és megjelenítése
    address = tk.Label(addressFrame, text= "Address", font=('Arial', 16))
    address.grid(row=0, column=0, sticky=tk.E+tk.W, padx=5, pady=0)

    # telefonszám szöveg létrehozása, keretbe rendezése és megjelenítése
    phoneNum = tk.Label(addressFrame, text= "Phone Number* (Numbers)", font=('Arial', 13))
    phoneNum.grid(row=1, column=0, sticky=tk.E+tk.W, padx=5, pady=20)
    # telefonszám bekérésére szolgáló textbox létrehozása, keretbe rendezése és megjelenítése
    inputPhoneNum = tk.Text(addressFrame, height=1, width=20,font=('Arial', 16))
    inputPhoneNum.grid(row=1, column=1, sticky=tk.E+tk.W, padx=0, pady=20)

    # utca szöveg létrehozása, keretbe rendezése és megjelenítése
    street = tk.Label(addressFrame, text= "Street* (Letters)", font=('Arial', 13))
    street.grid(row=2, column=0, sticky=tk.E+tk.W, padx=5, pady=0)
    # utca bekérésére szolgáló textbox létrehozása, keretbe rendezése és megjelenítése
    inputStreet = tk.Text(addressFrame, height=1, width=20, font=('Arial', 16))
    inputStreet.grid(row=2, column=1, sticky=tk.E+tk.W, padx=0, pady=0)

    # házsszám szöveg létrehozása, keretbe rendezése és megjelenítése
    houseNum = tk.Label(addressFrame, text= "House Number* (Numbers)", font=('Arial', 13))
    houseNum.grid(row=3, column=0, sticky=tk.E+tk.W, padx=5, pady=20)
    # házszám bekérésére szolgáló textbox létrehozása, keretbe rendezése és megjelenítése
    inputHouseNum = tk.Text(addressFrame, height=1, width=20,font=('Arial', 16))
    inputHouseNum.grid(row=3, column=1, sticky=tk.E+tk.W, padx=0, pady=20)

    # emelet szöveg létrehozása, keretbe rendezése és megjelenítése
    floorNum = tk.Label(addressFrame, text= "Floor (Numbers)", font=('Arial', 13))
    floorNum.grid(row=4, column=0, sticky=tk.E+tk.W, padx=5, pady=0)
    # házszám bekérésére szolgáló textbox létrehozása, keretbe rendezése és megjelenítése
    inputFloorNum = tk.Text(addressFrame, height=1, width=20,font=('Arial', 16))
    inputFloorNum.grid(row=4, column=1, sticky=tk.E+tk.W, padx=0, pady=0)

    global clicked

    #combox alapértelmezett szövegének beállítása
    clicked.set("Postal Code*")

    #combobox feltöltése opciókkal (irányítószám)
    comboboxPostalCode = ttk.Combobox(addressFrame, width=27, textvariable=clicked, state='readonly')
    comboboxPostalCode['values'] = ("1007", "1011", "1012", "1013", "1014", "1015", "1016", "1021", "1022", "1023", "1024", "1025",
                          "1026", "1027", "1028", "1029", "1031", "1032", "1033", "1034", "1035", "1036", "1037", "1038",
                          "1039", "1041", "1042", "1043", "1044", "1045", "1046", "1047", "1048", "1051", "1052", "1053",
                          "1054", "1055", "1056", "1061", "1062", "1063", "1064", "1065", "1066", "1067", "1068", "1071",
                          "1072", "1073", "1074", "1075", "1076", "1077", "1078", "1081", "1082", "1083", "1084", "1085",
                          "1086", "1087", "1088", "1089", "1091", "1092", "1093", "1094", "1095", "1096", "1097", "1098",
                          "1101", "1102", "1103", "1104", "1105", "1106", "1107", "1108", "1111", "1112", "1113", "1114",
                          "1115", "1116", "1117", "1118", "1119", "1121", "1122", "1123", "1124", "1125", "1126", "1131",
                          "1132", "1133", "1134", "1135", "1136", "1137", "1138", "1139", "1141", "1142", "1143", "1144",
                          "1145", "1146", "1147", "1148", "1149", "1151", "1152", "1153", "1154", "1155", "1156", "1157",
                          "1158", "1161", "1162", "1163", "1164", "1165", "1171", "1172", "1173", "1174", "1181", "1182",
                          "1183", "1184", "1185", "1186", "1188", "1191", "1192", "1193", "1194", "1195", "1196", "1201",
                          "1202", "1203", "1204", "1205", "1211", "1212", "1213", "1214", "1215", "1221", "1222", "1223",
                          "1224", "1225", "1237", "1238", "1239")

    #combobox elrendezése a keretben
    comboboxPostalCode.grid(row=5, column=1, sticky=tk.E+tk.W, padx=5, pady=20)
    comboboxPostalCode.current()

    # "addressFrame" keret megjelenítése
    addressFrame.pack()

    #cím mentése gomb létrehozása és megjelenítése
    buttonSubmit = tk.Button(root, text="Submit", height=1, width=7, font=('Arial', 16), bg="green", fg="white", command=tab2)
    buttonSubmit.pack(padx=0, pady=20)

#1 oldal megnyitása (tab1 metódus meghívása)
tab1()

root.mainloop()