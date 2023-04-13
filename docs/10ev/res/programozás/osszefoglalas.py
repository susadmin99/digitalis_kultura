#if(elágazás)
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

#for loop(ciklus)
for alma in "Alma":
    print(alma)

for korte in range(10):
    print(korte)

for eper in range(10,20):
    print(eper)

for repa in range(10,50,2):
    print(repa)
else:
    print("Vége")

#while loop(ciklus)
x = 10
while x < 20:
    print(x)
    x+=1
else:
    print("Vége")
    
#listák
egy_lista = ["első", "második", "harmadik", "negyedik", "ötödik"]
szamok = [1, 2, 3, 4, 5]
logika = [True, True, False, True, False]
minden_is = ["első", 4, True, "hatvan", False, 42]
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

#függvények(function)
print("Hello...")

def welcome():
    print("Welcome...")

#welcome()

print("----------1----------")
def say_your_name(your_name):
    print(f"Hello {your_name}")

say_your_name("Bob")
say_your_name("Emily")
say_your_name("Linus")

print("----------2----------")
def more_names(name1, name2, name3):
    print(name1 + ", " + name2 + ", " + name3)

more_names("Olivia", "Katrine", "Harold")

print("----------3----------")
def default(num = 10):
    print(num**2)

default()
default(20)

print("----------4----------")
def list_function(random_list):
    for i in random_list:
        print(i)

my_list = [2, 4, 6, 8, 10]
my_second_list = ["Amsterdam", "Brussels", "Paris", "Berlin", "Vienna", "Budapest",]

list_function(my_list)
list_function(my_second_list)

print("----------5----------")
def return_function(num):
    return 10 * num

my_number = return_function(10)
print(return_function(20))

print("----------6----------")
def empty_function():
    pass

empty_function()