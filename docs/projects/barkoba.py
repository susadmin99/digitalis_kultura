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