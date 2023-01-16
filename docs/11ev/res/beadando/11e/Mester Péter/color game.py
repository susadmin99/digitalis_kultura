"Gondoltam egy számra" játék
#A véletlenszám generáláshoz használt függvények betöltése
import random
#Változók létrehozása a memóriában, eredeti értékek megadása
gondoltszam = random.randint(1,100)
tipp = 0
lepes = 0
print('Gondoltam egy számra 1 és 100 között, találd ki!')
print()
#Előltesztelő ciklus: addig kérdez amíg el nem találja a számot
while tipp != gondoltszam:
 lepes = lepes + 1 # lépésszámláló növelése
 tippszoveg = input('Kérlek add meg a tipped: ') #A tipp bekérése
 #Szöveg átalakítása számmá, mivel az input szöveget ad vissza
 tipp = int(tippszoveg)
 
 #Feltételek: mit írjon ki ha nagyobb, vagy ha kisebb a szám
 if tipp < gondoltszam:
 print ('Sajnálom, a szám nagyobb!')
 if tipp > gondoltszam:
 print ('Sajnálom, a szám kisebb!')
 print() #Üres sor beszúrása az esztétikum miatt
#Eltatálta a számot, tovább lehet lépni
print('Gratulálok, eltaláltad a számot',str(lepes),'lépésből!')
print()