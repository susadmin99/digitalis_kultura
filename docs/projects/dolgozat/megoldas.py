orvos_nev = input("Kezelőorvos neve: ") # Tamás
datum = input("Mai dátum: ") # Tamás

# calculate bmi
def bmi_calc(suly, magassag): # bmi = súly/magasság**2
    return int(suly)/((int(magassag)/100)**2)

def bmi_type(bmi): # milyen a bmi tipusa
    if bmi < 18.5:
        return "Under weight"
    elif bmi > 18.5 and bmi < 24.9:
        return "Normal weight"
    elif bmi > 24.9 and bmi < 29.9:
        return "Overweight"
    elif bmi > 29.9 and bmi < 34.9:
        return "Obese 1"
    elif bmi > 34.9 and bmi < 39.9:
        return "Obese 2"
    elif bmi > 39.9:
        return "Obese 3"

# kérj be egy 10 nevet egy listára
# kérj be 10 nem-et egy listára
# kérj be 10 magasságot egy listára

betegszam = int(input("Betegek száma: "))

nevek = []
nemek = []
magassagok = []
sulyok = []

for i in range(betegszam):
    print("Következő beteg...")
    nevek.append(input("Neve: "))
    nemek.append(input("Neme: "))
    magassagok.append(input("Magassága(cm): "))
    sulyok.append(input("Súlya: "))
    
bmik = []
for i in range(len(nevek)):
    bmik.append(bmi_calc(sulyok[i], magassagok[i]))

print(f"Az orvos neve: {orvos_nev}")
print(f"Mai dátum: {datum}")
for i in range(len(bmik)):
    print(bmi_type(bmik[i]))
