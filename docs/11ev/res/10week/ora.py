import tkinter as tk

#1. felvonás
window = tk.Tk()

def say_hello():
    label2.config(text="Hello")

def say_my_name():
    label2.config(text=f"Hello {entry1.get()}")

btn1 = tk.Button(text="Say hello", command=say_hello)

label1 = tk.Label(text="Name please:")
entry1 = tk.Entry()
btn2 = tk.Button(text="Say my name", command=say_my_name)
label2 = tk.Label()

btn1.pack()
label1.pack()
entry1.pack()
btn2.pack()
label2.pack()

window.mainloop()

#feladat
login_status = "You are not logged in!"
def login():
    if username_entry.get() == "admin" and password_entry.get() == "admin123":
        login_status = "Successful login!"
        login_label.config(text=login_status)
    else:
        login_status = "Wrong credentials! Try again!"
        login_label.config(text=login_status)

fl = tk.Tk()
fl.geometry("300x150")

username_label = tk.Label(text="Username")
username_entry = tk.Entry()

password_label = tk.Label(text="Password")
password_entry = tk.Entry(show="*")

login_btn = tk.Button(text="Login", command=login)
login_label = tk.Label(text=login_status)

username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
login_btn.pack()
login_label.pack()

fl.mainloop()

#2. felvonás
fl2 = tk.Tk()

#canvas
cv = tk.Canvas(fl2, bg="grey", height=100, width=300)
coord = 5, 5, 250, 150
arc = cv.create_arc(coord, start=0, extent=150, fill="black")

#check button
cb = tk.Checkbutton(fl2, text="Test Check Button")

#listbox
lb = tk.Listbox(fl2)
lb.insert(1, "Python")
lb.insert(2, "C#")
lb.insert(3, "Java")
lb.insert(4, "Kotlin")
lb.insert(5, "C++")
lb.insert(6, "PHP")

#menu
menubar = tk.Menu(fl2)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
file_menu.add_command(label="Save as...")
file_menu.add_command(label="Close")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=fl2.quit)

menubar.add_cascade(label="File", menu=file_menu)

edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo")

edit_menu.add_separator()

edit_menu.add_command(label="Cut", )
edit_menu.add_command(label="Copy", )
edit_menu.add_command(label="Paste", )
edit_menu.add_command(label="Delete", )
edit_menu.add_command(label="Select All", )

menubar.add_cascade(label="Edit", menu=edit_menu)

#message
szoveg = "Hello, én egy szöveg vagyok!!!"
message = tk.Message(fl2, text=szoveg)

#radiobutton
radio = tk.Radiobutton(fl2, text="Egy almafa", value=1)

radio2 = tk.Radiobutton(fl2, text="Két kiskacsa", value=2)

#scale
scale = tk.Scale( fl2)

#spinbox
sb = tk.Spinbox(fl2, from_=0, to=10)


cv.pack()
cb.pack()
lb.pack()
message.pack()
radio.pack()
radio2.pack()
scale.pack()
sb.pack()

fl2.config(menu=menubar)
fl2.mainloop()

