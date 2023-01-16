import tkinter as tk
from tkinter import *

#button_1 funkcióját megadó függvény:
def encode_decode():
    if label_1['text']=='E':
        #üres lista
        xyz=[]
        #rendes (angol) abc
        abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","0","1","2","3","4","5","6","7","8","9",","]
        #titkos nyelvű abc
        cba=["o","p","z","g","u","y","d","q","e","l","t","j","m","n","i","b","h","r","s","k","a","w","v","x","f","c"," ","0","1","2","3","4","5","6","7","8","9",","]
        encode = input_1.get()
        #lekicsinyíti a betűket - h ne okozzon problémát a nagybetű
        for i in encode.lower():
            #végigmegy a kisbetűs input karakterein
            for x in abc:
                #végigmegy az abc lista karakterein
                if i==x:
                #ha a kettő megegyezik, akkor beleteszi az üres listába a másik féle abc-ből az eredetivel megegyező indexű karaktert
                    xyz.append(cba[abc.index(x)])
        #szöveggé alakítja a listát
        decode = ""
        for i in xyz:
            decode+=i
        text_1['text']= decode
    #az előbbi fordítottja    
    else:
        xyz=[]
        #titkos nyelvű abc
        abc=["o","p","z","g","u","y","d","q","e","l","t","j","m","n","i","b","h","r","s","k","a","w","v","x","f","c"," ","0","1","2","3","4","5","6","7","8","9",","]
        #rendes (angol) abc
        cba=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","0","1","2","3","4","5","6","7","8","9",","]
        decode = input_1.get()
        for i in decode.lower():
            for x in abc:
                if i==x:
                    xyz.append(cba[abc.index(x)])
        encode = ""
        for i in xyz:
            encode+=i
        text_1['text']= encode

#button_2 funkcióját megadó függvény:
def reverse():
    #megcseréli, hogy kódolni/dekódolni akarunk e
    if label_1['text']=='E':
        label_1['text']='D'
        label_2['text']='E'
    else:
        label_1['text']='E'
        label_2['text']='D'

#magának az ablaknak egyes tulajdonságait adja meg
window = tk.Tk()
#címét/nevét
window.title('Encode/Decode')
#méretét
window.geometry("275x200")
#színét
window.configure(bg='#9cb8e6')

#.Label kiírja a megadott szöveget (text=' ') *
label_0 = tk.Label(text='Welcome!', width=10)
label_1 = tk.Label(text='E', width=35)

#.Entry bekér szöveget
input_1 = tk.Entry(master =window, width=35, bd=4)

#.Button gombok, adott funkcióval ellátva (command=)
button1 = tk.Button(text="\N{DOWNWARDS BLACK ARROW}", command=encode_decode, width=25)
#az encode_decode függvényt alkalmazza
button2 = tk.Button(text='\N{CLOCKWISE RIGHTWARDS AND LEFTWARDS OPEN CIRCLE ARROWS}', command=reverse)
#a reverse függvényt alkalmazza

label_2 = tk.Label(text='D', width=35) # *
text_1 = tk.Label(text='', width=35,bg="#9bd1d1", relief="sunken")

#width= - szélességet állít be
#relief= - körvonalat/keretet állít be
#bg= - hátteret állít be

#becsomagolja (.grid olyasmi, mint a .pack) - így jelennek meg a fenti gombok, szövegek stb.
label_0.grid(row=0, column=0)
label_1.grid(row=1, column=0)
input_1.grid(row=2, column=0)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
label_2.grid(row=4, column=0)
text_1.grid(row=5, column=0)

window.mainloop()