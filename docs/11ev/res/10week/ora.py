import tkinter as tk

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




