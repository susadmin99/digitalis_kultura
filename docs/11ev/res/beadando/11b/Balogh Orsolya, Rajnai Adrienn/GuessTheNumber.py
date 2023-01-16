#Ez egy könyvtár, amit beimportáljuk hogy tudjuk random számot generálni
import random

#Kiíratások
print("Ez egy szám kitalálós program. 1-től 100-ig generál egy számot, amit ki kell találnod")
print("Ha ki akarsz lépni a programból, akkor írd be ezt: 'kilépés' parancsot")
print("Ha fel szeretnéd adni, akkor írd be ezt: 'feladom' parancsot")
#Egy ciklus, ami addig megy, amíg a felhasználó játszani kíván a játékkal
while True:
    #Élet megadásához egy ciklus
    while True:
        print("A játék elkezdéséhez add meg hány darab életed legyen")
        health = input()
        try:
            health = int(health)
            break
        except:
            print("Számot adj meg!")
    print("Szám legenerálva")
    #Itt generál egy számot, amit ki kell találni
    r = random.randint(1, 100)
    while True:
        #Lekérdezzük hogy nagyobb-e az élete mint 0, ha igen akkor folytathatja a játékot, ha nem akkor megírja a program a helyes választ és kezdhet egy új játékot, ha akar
        if health > 0:
            print("Találgass")
            #Bekérjük a találgatást
            guess = input()
            #Ha számon kívül bármi mást adna meg, akkor azt lekezeljük
            try:
                #Megpróbáljuk átkonvertálni int típusúvá
                guess = int(guess)
                #Ha a szám, amit tippelt megegyezik a generált számmal
                if r == guess:
                    print("Sikeresen eltaláltad!")
                    #Ha új játékot akar kezdeni, akkor be kell írni az igen-t
                    print("Szeretnél új játékot kezdeni? Ha igen, akkor írj be ezt: 'igen', ha nem akkor bármi mást")
                    newgame = input()
                    #Ha az igen-t írta be, akkor kilép a ciklusból  és kezd egy új játékot
                    if newgame.lower() == "igen":
                        break
                    else:
                        break
                #Ha a beírt szám kisebb mint a generált szám, akkor jelzi neked hogy nagyobb
                elif r > guess:
                    print("Nagyobb")
                    health -= 1
                # Ha a beírt szám nagyobb mint a generált szám, akkor jelzi neked hogy kisebb
                elif r < guess:
                    print("Kisebb")
                    health -= 1
            #Ha nem számot adott meg, akkor megnézzük hogy esetleg a 'kilépés' vagy a 'feladom' parancsot használta e, ha nem akkor jelezzük hogy számot adjon meg
            except:
                if guess == "kilépés":
                    break
                elif guess == "feladom":
                    print("Helyes válasz " + str(r))
                    print("Szeretnél új játékot kezdeni? Ha igen, akkor írj be ezt: 'igen', ha nem akkor bármi mást")
                    newgame = input()
                    # Ha az igen-t írta be, akkor kilép a ciklusból és kezd egy új játékot
                    if newgame == "igen":
                        break
                    else:
                        break
                else:
                    print("Számot adj meg!")
        else:
            #Ha elfogynak az életei akkor ez az ág fut le
            print("Meghaltál. Elfogytak az életeid")
            print("Helyes válasz " + str(r))
            print("Szeretnél új játékot kezdeni? Ha igen, akkor írj be ezt: 'igen', ha nem akkor bármi mást")
            newgame = input()
            # Ha az igen-t írta be, akkor kilép a ciklusból és kezd egy új játékot
            if newgame.lower() == "igen":
                break
            else:
                break
    #Leellenőrzőm hogy mi volt a szándéka, ha a 'kilépés' parancsot írta be, vagy ha előtte a játék felajánlotta, hogy szeretne egy új játékot, de a felhasználó elutasította, akkor kilép a fő ciklusból
    if guess == "kilépés" or newgame != "igen":
        break
#Ha már nincs kedvük játszani, akkor kiírja ezt az üzenetet
print("Game over")