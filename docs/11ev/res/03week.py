ablak = 10
print(ablak)

ajto = int(input("Ajtó mérete: "))
print(ablak + ajto)

if ajto == 20:
    print("Az ajtó az 20.")
    print(ablak*ajto)
elif ajto == 30:
    print("Az ajtó az 30.")
    print(ablak/ajto)
else:
    print(f"Az ajtó: {ajto}")

print(ajto == 30)