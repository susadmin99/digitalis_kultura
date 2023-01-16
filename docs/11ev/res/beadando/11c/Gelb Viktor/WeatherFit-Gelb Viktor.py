#összeszedtem általános ruhadarabokat, nyilván bővíthető ez még
elfogadottruhak = ("trikó", "rövidujjú póló", "hosszúujjú póló","ing/blúz", "garbó", "kardigán", "pulóver", "mellény", "dzseki" ,"kabát" )
elfogadottruhak1 = ("rövidnadrág", "nejlonharisnya", "vastag harisnya", "leggings", "farmernadrág","melegítőnadrág", "overál" )
lábbelik = ("papucs", "szandál", "trainer", "sneaker", "bakancs", "bokacsizma", "hosszúcsizma", "gumicsizma")
extrák = ("sapka", "sál", "kesztyű",)
#csináltam egy külön listát a személy által kijelölt ruhadaraboknak
felsoim = list()
nadragjaim = list()
cipőim = list()
extráim = list()
#csoportosítottam a ruhadarabokat attól függően, hogy milyen hőmérsékleten hordanám azt
nullaalatt = list()
otalatt = list()
otfelett = list()
tizalatt = list()
tizenotalatt = list()
tizenotfelett = list()
huszalatt = list()
huszfelett = list()
huszonotalatt = list()
huszonotfelett = list()
harmincfelett = list()
harmincalatt = list()
mindig = list()
#hozzáadtam ezeket a ruhadarabokat a hordási hőmérsékletükhöz az indexeket használva
nullaalatt.append(extrák[2])
nullaalatt.append(elfogadottruhak1[6])
otalatt.append(elfogadottruhak[4])
otalatt.append(elfogadottruhak1[2])
otalatt.append(lábbelik[6])
otalatt.append(extrák[1])
tizalatt.append(elfogadottruhak[2])
tizalatt.append(elfogadottruhak[9])
tizalatt.append(lábbelik[4])
tizalatt.append(lábbelik[5])
tizalatt.append(extrák[0])
tizenotalatt.append(elfogadottruhak[8])
tizenotfelett.append(elfogadottruhak[0])
huszalatt.append(elfogadottruhak[5])
huszalatt.append(elfogadottruhak[6])
huszalatt.append(elfogadottruhak[7])
huszfelett.append(lábbelik[1])
huszonotalatt.append(elfogadottruhak[3])
huszonotalatt.append(elfogadottruhak1[1])
huszonotalatt.append(elfogadottruhak1[5])
huszonotfelett.append(elfogadottruhak1[0])
harmincalatt.append(elfogadottruhak1[3])
harmincalatt.append(elfogadottruhak1[4])
harmincfelett.append(lábbelik[0])
otfelett.append(lábbelik[2])
otfelett.append(lábbelik[3])
otfelett.append(elfogadottruhak[1])
#hozzáadtam a kisebb listákat a nagyobbakhoz
otalatt.append(nullaalatt)
tizalatt.append(nullaalatt)
tizalatt.append(otalatt)
tizalatt.append(otfelett)
tizenotalatt.append(nullaalatt)
tizenotalatt.append(otalatt)
tizenotalatt.append(otfelett)
tizenotalatt.append(tizalatt)
tizenotfelett.append(nullaalatt)
tizenotfelett.append(otalatt)
tizenotfelett.append(otfelett)
tizenotfelett.append(tizalatt)
tizenotfelett.append(tizenotalatt)
huszalatt.append(nullaalatt)
huszalatt.append(otalatt)
huszalatt.append(otfelett)
huszalatt.append(tizalatt)
huszalatt.append(tizenotalatt)
huszalatt.append(tizenotfelett)
huszfelett.append(nullaalatt)
huszfelett.append(otalatt)
huszfelett.append(otfelett)
huszfelett.append(tizalatt)
huszfelett.append(tizenotalatt)
huszfelett.append(tizenotfelett)
huszfelett.append(huszalatt)
huszonotalatt.append(nullaalatt)
huszonotalatt.append(otalatt)
huszonotalatt.append(otfelett)
huszonotalatt.append(tizalatt)
huszonotalatt.append(tizenotalatt)
huszonotalatt.append(tizenotfelett)
huszonotalatt.append(huszalatt)
huszonotalatt.append(huszfelett)
huszonotfelett.append(nullaalatt)
huszonotfelett.append(otalatt)
huszonotfelett.append(otfelett)
huszonotfelett.append(tizalatt)
huszonotfelett.append(tizenotalatt)
huszonotfelett.append(tizenotfelett)
huszonotfelett.append(huszalatt)
huszonotfelett.append(huszfelett)
huszonotfelett.append(huszonotalatt)
harmincalatt.append(nullaalatt)
harmincalatt.append(otalatt)
harmincalatt.append(otfelett)
harmincalatt.append(tizalatt)
harmincalatt.append(tizenotalatt)
harmincalatt.append(tizenotfelett)
harmincalatt.append(huszalatt)
harmincalatt.append(huszfelett)
harmincalatt.append(huszonotalatt)
harmincalatt.append(huszonotfelett)
harmincfelett.append(nullaalatt)
harmincfelett.append(otalatt)
harmincfelett.append(otfelett)
harmincfelett.append(tizalatt)
harmincfelett.append(tizenotalatt)
harmincfelett.append(tizenotfelett)
harmincfelett.append(huszalatt)
harmincfelett.append(huszfelett)
harmincfelett.append(huszonotalatt)
harmincfelett.append(huszonotfelett)
#bekértem bevásárlólistaszerűen a személy által birtokolt ruhadarabokat(bánom már, hogy nem egy sima bevásárlólistát csináltam)
print(elfogadottruhak)
felso = (input("Add meg a listából egyesével, mely felsőid vannak neked, ha végeztél, írd, hogy ennyi: "))
while felso != "ennyi":
    felsoim.append(felso)
    felso = (input("Add meg a következő ruhadarabot: "))
else:
    print(elfogadottruhak1)
nadrag = (input("Add meg a listából egyesével, mely nadrágjaid vannak neked, ha végeztél,írd, hogy ennyi: "))
while nadrag != "ennyi":
    nadragjaim.append(nadrag)
    nadrag = (input("Add meg a következő ruhadarabot: "))
else:
    print(lábbelik)
lábbeli = (input("Add meg a listából egyesével, mely lábbelijeid vannak neked, ha végeztél,írd, hogyennyi: "))
while lábbeli != "ennyi":
    cipőim.append(lábbeli)
    lábbeli =  (input("Add meg a következő ruhadarabot: "))
else:
    print(extrák)
extra = (input("Add meg a listából egyesével, mely extráid vannak neked, ha végeztél,írd, hogy ennyi: "))
while extra != "ennyi":
    extráim.append(extra)
    extra = input("Add meg a következő ruhadarabot: ")
#lista a végeredményhez
hordható = list()
homerseklet = int(input("Add meg a hőmérsékletet: "))

if homerseklet <= 5:
    for felsom in otalatt:
        if felsom in felsoim and felsom not in hordható:
            hordható.append(felsom)
    for nadrag in otalatt:
        if nadrag in nadragjaim and nadrag not in hordható:
            hordható.append(nadrag)
    for cipo in otalatt:
        if cipo in cipőim and cipo not in hordható:
            hordható.append(cipo)
    for extra in otalatt:
        if extra in extráim and extra not in hordható:
            hordható.append(extra) 
if homerseklet >= 5:
    for felsom in otfelett:
        if felsom in felsoim and felsom not in hordható:
            hordható.append(felsom)
    for nadrag in otfelett:
        if nadrag in nadragjaim and nadrag not in hordható:
            hordható.append(nadrag)
    for cipo in otfelett:
        if cipo in cipőim and cipo not in hordható:
            hordható.append(cipo)
    for extra in otfelett:
        if extra in extráim and extra not in hordható:
            hordható.append(extra)            
if homerseklet <= 10:
    for felsom in tizalatt:
        if felsom in felsoim and felsom not in hordható:
            hordható.append(felsom)
    for nadrag in tizalatt:
        if nadrag in nadragjaim and nadrag not in hordható:
            hordható.append(nadrag)
    for cipo in tizalatt:
        if cipo in cipőim and cipo not in hordható:
            hordható.append(cipo)
    for extra in tizalatt:
        if extra in extráim and extra not in hordható:
            hordható.append(extra)
if homerseklet <=15 :
    for felsom in tizenotalatt:
        if felsom in felsoim and felsom not in hordható:
            hordható.append(felsom)
    for nadrag in tizenotalatt:
        if nadrag in nadragjaim and nadrag not in hordható:
            hordható.append(nadrag)
    for cipo in tizenotalatt:
        if cipo in cipőim and cipo not in hordható:
            hordható.append(cipo)
    for extra in tizenotalatt:
        if extra in extráim and extra not in hordható:
            hordható.append(extra)
if homerseklet >=15:
    for felsom in tizenotfelett:
        if felsom in felsoim and felsom not in hordható:
            hordható.append(felsom)
    for nadrag in tizenotfelett:
        if nadrag in nadragjaim and nadrag not in hordható:
            hordható.append(nadrag)
    for cipo in tizenotfelett:
        if cipo in cipőim and cipo not in hordható:
            hordható.append(cipo)
    for extra in tizenotfelett:
        if extra in extráim and extra not in hordható:
            hordható.append(extra)
if homerseklet <= 20:
    for felsom in huszalatt:
        if felsom in felsoim and felsom not in hordható:
            hordható.append(felsom)
    for nadrag in huszalatt:
        if nadrag in nadragjaim and nadrag not in hordható:
            hordható.append(nadrag)
    for cipo in huszalatt:
        if cipo in cipőim and cipo not in hordható:
            hordható.append(cipo)
    for extra in huszalatt:
        if extra in extráim and extra not in hordható:
            hordható.append(extra)
if homerseklet >= 20:
    for felsom in huszfelett:
        if felsom in felsoim and felsom not in hordható:
            hordható.append(felsom)
    for nadrag in huszfelett:
        if nadrag in nadragjaim and nadrag not in hordható:
            hordható.append(nadrag)
    for cipo in huszfelett:
        if cipo in cipőim and cipo not in hordható:
            hordható.append(cipo)
    for extra in huszfelett:
        if extra in extráim and extra not in hordható:
            hordható.append(extra)
if homerseklet <= 25:
    for felsom in huszonotalatt:
        if felsom in felsoim and felsom not in hordható:
            hordható.append(felsom)
    for nadrag in huszonotalatt:
        if nadrag in nadragjaim and nadrag not in hordható:
            hordható.append(nadrag)
    for cipo in huszonotalatt:
        if cipo in cipőim and cipo not in hordható:
            hordható.append(cipo)
    for extra in huszonotalatt:
        if extra in extráim and extra not in hordható:
            hordható.append(extra)
if homerseklet >= 25:
    for felsom in huszonotfelett:
        if felsom in felsoim and felsom not in hordható:
            hordható.append(felsom)
    for nadrag in huszonotfelett:
        if nadrag in nadragjaim and nadrag not in hordható:
            hordható.append(nadrag)
    for cipo in huszonotfelett:
        if cipo in cipőim and cipo not in hordható:
            hordható.append(cipo)
    for extra in huszonotfelett:
        if extra in extráim and extra not in hordható:
            hordható.append(extra)
if homerseklet <= 30:
    for felsom in harmincalatt:
        if felsom in felsoim and felsom not in hordható:
            hordható.append(felsom)
    for nadrag in harmincalatt:
        if nadrag in nadragjaim and nadrag not in hordható:
            hordható.append(nadrag)
    for cipo in harmincalatt:
        if cipo in cipőim and cipo not in hordható:
            hordható.append(cipo)
    for extra in harmincalatt:
        if extra in extráim and extra not in hordható:
            hordható.append(extra)
if homerseklet >= 30:
    for felsom in harmincfelett:
        if felsom in felsoim and felso not in hordható:
            hordható.append(felsom)
    for nadrag in harmincfelett:
        if nadrag in nadragjaim and nadrag not in hordható:
            hordható.append(nadrag)
    for cipo in harmincfelett:
        if cipo in cipőim and cipo not in hordható:
            hordható.append(cipo)
    for extra in harmincfelett:
        if extra in extráim and extra not in hordható:
            hordható.append(extra)


print (f"A hőmérsékletet tekintve mára ajánlott a következő ruhákből válogatni: {hordható}")
        

