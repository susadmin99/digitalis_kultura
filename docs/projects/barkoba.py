import random

print("Játszunk egy kis barkóbat. Gondolok egy számra 1 és 100 között. Találd ki...")

gondolt_szam = random.randint(1,100)
megvan = False

while megvan == False:
    tipp = int(input("Tippelj egy számot: "))
    if (tipp != gondolt_szam and tipp > gondolt_szam):
         print("A szám amire gondoltál az nagyobb, mint a megoldás.")
    elif (tipp != gondolt_szam and tipp < gondolt_szam):
        print("A szám amire gondoltál az kisebb, mint a megoldás.")
    elif tipp == gondolt_szam:
        print("YEEEEEEY Eltaláltad!")
        megvan = True






















gyumolcsok = ["alma", "eper", "füge", "mangó", "cseresznye", "kiwi"]
print("A lista utolsó eleme:")
print(gyumolcsok[-1])

print("A lista hossza:")
print(len(gyumolcsok))

szamok2 = [10, 20, 30, 40, 50, 60, 	70, 80, 90]
osszeg = 0
for valami in szamok2:
    osszeg += valami