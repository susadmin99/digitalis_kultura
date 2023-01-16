import math


# primszámvizsgálat 2-tõl a szám négyzetgyökének lefele kerekített egész számáig egy ciklus és ha osztás után nincs maradék akkor nem prím
def prim(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# faktoriális számítás, rekurzív módszer, bemenetet szorozza bemenet-1 -el
def faktorialis(n):
    if n == 0:
        return 1
    else:
        return n * faktorialis(n-1)

# radián ból fok számítás (radián*180/pi)
def radfok(radian):
    return radian*(180/math.pi)

while True:
    try:
        print()
        szam1 = float(input("Kérek egy számot: "))
        muv = input("Mûvelet (+, -, *, /, sin, cos, gyok, fok, prim, fakt): ")
        if muv in ['sin','cos','gyok','fok','prim','fakt']:
            if muv == 'sin':
                result = math.sin(szam1)
                print("sin(", szam1, ")=", result)
            elif muv == 'cos':
                result = math.cos(szam1)
                print("cos(", szam1, ")=", result)
            elif muv == 'gyok':
                result = math.sqrt(szam1)
                print("gyok(", szam1, ")=", result)
            elif muv == 'fok':
                result = radfok(szam1)
                print(szam1, "radian = ", result, "fok")
            elif muv == 'prim':
                if prim(szam1):
                    print(szam1, " egy primszam.")
                else:
                    print(szam1, " nem primszam.")
            elif muv == 'fakt':
                result = faktorialis(szam1)
                print(szam1, "! = ", result)
        else:
            szam2 = float(input("Kérek még egy számot: "))
            if muv == "+":
                result = szam1 + szam2
                print(szam1, "+", szam2, "=", result)
            elif muv == "-":
                result = szam1 - szam2
                print(szam1, "-", szam2, "=", result)
            elif muv == "*":
                result = szam1 * szam2
                print(szam1, "*", szam2, "=", result)
            elif muv == "/":
                if szam2 == 0:
                    print("HIBA: nullával nem lehet osztani.")
                else:
                    result = szam1 / szam2
                    print(szam1, "/", szam2, "=", result)
            else:
                print("HIBA: Ismeretlen mûvelet.")
    except ValueError:
        print("HIBA: Nem értelmezhetõ szám.")
    except:
        print("HIBA: Ismeretlen hiba.")
