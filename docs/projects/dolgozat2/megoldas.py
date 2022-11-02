print("2.feladat")
szam = int(input("Adj meg egy számot: "))
nev = input("Adj meg egy nevet: ")

print(szam)
print(nev)

print("3.feladat")
if szam > 365:
    print(szam/365)
else:
    print(szam)

print("4.feladat")
for i in nev:
    print(i)

print("5.feladat")
varos_nevek = ["Budapest", "Párizs", "Berlin", "Toronto", "Amszterdam", "Peking"]
for i in varos_nevek:
    print(varos_nevek)

print("+1.feladat")
varos_nevek.append(input("Adj meg egy városnevet: "))
print(varos_nevek) #nem kötelező kiíratni