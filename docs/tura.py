import random

tura_vezeto = input("Túravezető neve: ")
turazok_szama = int(input("Túrázók száma (maximum 20 fő): "))

if turazok_szama > 10:
    print(f"Két csoportos túra lesz. Túrázók száma: {turazok_szama}")
else:
    print(f"Egy csoportos túra lesz. Túrázók száma: {turazok_szama}")

tura_varosok = []
tura_varosok.append("Budapest")
tura_varosok.append("Bécs")
tura_varosok.append("Pozsony")

print("Választható helyszínek:")
for varos in tura_varosok:
    print(varos)

tura_varosok_random = random.choice(tura_varosok)
print(
    f"A következő túra {turazok_szama} fős lesz. A túravezető: {tura_vezeto}. A túra helyszíne: {tura_varosok_random}.")
