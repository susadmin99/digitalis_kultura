#Bevásárlólista alkalmazás

bevasarlolista = list()

#Négy funkció közül lehet választani a listakeszítés során, a listához hozzáadni, elvenni, megjeleníteni az egész listát, illetve kilépni az alkalmazásból

while True:
    print("Listafunkciók: felvinni (1), törölni (2),  \
    listázni (3) és kilépni(4)")
    valasztas = input("Válassz egy számot: ")
#Az 1-es gombbal tudunk hozzáadni a listához

    if valasztas == "1":
        termek = input("Add meg a termék nevét amit felviszel: ")
        bevasarlolista.append(termek)

#A 2-es gombbal elvenni tudunk a listából

    elif valasztas == "2":
        for index in range( len(bevasarlolista) ):
            print(f"{index} - {bevasarlolista[index]} ")
        torlendo = int(input("Add meg a termék indexét, amit törölnél: "))
        bevasarlolista.pop(torlendo)

#A 3-as gombbal meg tudjuk jeleníteni a teljes listánkat

    elif valasztas == "3":
        print("A bevásárlólista elemei: ")
        for elem in bevasarlolista:
            print(elem)
        ossz = len(bevasarlolista)
        print(f"A listádban {ossz} elem van")

#A 4-es gombbal ki tudunk lépni az alkalmazásból

    elif valasztas == "4":
        break

