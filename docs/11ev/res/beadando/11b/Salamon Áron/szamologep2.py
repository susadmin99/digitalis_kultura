import math



def prim(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# faktori�lis sz�m�t�s, rekurz�v m�dszer, bemenetet szorozza bemenet-1 -el
def faktorialis(n):
    if n == 0:
        return 1
    else:
        return n * faktorialis(n-1)

# radi�n b�l fok sz�m�t�s (radi�n*180/pi)
def radfok(radian):
    return radian*(180/math.pi)

while True:
    try:
        print()
        szam1 = float(input("K�rek egy sz�mot: "))
        muv = input("M�velet (+, -, *, /, sin, cos, gyok, fok, prim, fakt): ")
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
            szam2 = float(input("K�rek m�g egy sz�mot: "))
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
                    print("HIBA: null�val nem lehet osztani.")
                else:
                    result = szam1 / szam2
                    print(szam1, "/", szam2, "=", result)
            else:
                print("HIBA: Ismeretlen m�velet.")
    except ValueError:
        print("HIBA: Nem �rtelmezhet� sz�m.")
    except:
        print("HIBA: Ismeretlen hiba.")
