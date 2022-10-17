










egy_lista = ["első", "második", "harmadik", "negyedik", "ötödik"]
szamok = [1, 2, 3, 4, 5]
logika = [True, True, False, True, False]
minden_is = ["első", 4, True, "hatvan", False, 42.76]
hmmm = [["egy", "kettő", "három"], [1, 2, 3]]

print(len(logika))

print(szamok[2])

print(egy_lista[-1])

print(minden_is[2:4])
print(szamok[:3])
print(szamok[2:])

if "második" in egy_lista:
    print("Az elem: 'másodiK' benne van a listában.")

szamok[0] = 55
print(szamok)

szamok.insert(3, 999)
szamok.append(101010)
print(szamok)

egy_lista.remove("harmadik")
egy_lista.pop(2)
print(egy_lista)

for elem in szamok:
    print(elem)

sorrend = [12, 56, 23, 89, 124, 845, 34, 1]
sorrend.sort()
print(sorrend)

sorrend.sort(reverse = True)
print(sorrend)

listavok = [["x","x","x"],["x","x","x"],["x","x","x"]]
for elem in listavok:
    print(elem)













szo = input("Adj meg egy szót: ")
index = 0
for betu in szo:
    if betu == "a":
        print(index)
    index += 1



szam = int(input("Adj meg egy számot 20-50 között: "))
for valami in range(szam, 101):
    print(valami)