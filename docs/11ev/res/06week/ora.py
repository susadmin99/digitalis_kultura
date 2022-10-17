













print("Hello...")

def welcome():
    print("Welcome...")

welcome()

print("----------1----------")
def say_your_name(your_name):
    print(f"Hello {your_name}")

say_your_name("Bob")
say_your_name("Emily")
say_your_name("Linus")

print("----------2----------")
def more_names(name1, name2, name3):
    print(name1 + ", " + name2 + ", " + name3)
    print(f"{name1}, {name2}, {name3}")

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
my_second_list = ["Amsterdam", "Brussels", "Paris", "Berlin", "Vienna", "Budapest"]

list_function(my_list)
list_function(my_second_list)
list_function("szöveg")

print("----------5----------")
def return_function(num):
    return 10 * num

my_number = return_function(10)
print(return_function(20))

print("----------6----------")
def empty_function():
    pass

empty_function()

for valami in range(10):
    print(valami)

for meg_valami in "alma":
    print(meg_valami)


























