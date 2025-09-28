# python_projektit
Erilaisia python-koodilla tehtyjä projekteja



# Peruskäsitteet python-ohjelmointikielessä:

Muuttuja (variable) Säilöö tietoa ohjelman ajaksi. Esim. nimi = "Antti" tallentaa tekstin muuttujaan nimi.

Tietotyypit (data types) Pythonissa yleisiä tyyppejä ovat:

int (kokonaisluku)

float (desimaaliluku)

str (merkkijono)

bool (totuusarvo: True tai False)

list, tuple, dict, set (tietorakenteet)

Funktio (function) Koodin uudelleenkäytettävä lohko. Esim.:

python
def tervehdi(nimi):
    print(f"Hei, {nimi}!")
Komentotulkki (interpreter) Python on tulkattu kieli, eli koodi suoritetaan rivi riviltä ilman erillistä käännöstä.

🔁 Ohjausrakenteet
Ehtolauseet (if, elif, else) Mahdollistavat päätöksenteon:

python
if x > 0:
    print("Positiivinen")
Silmukat (for, while) Toistavat koodia:

python
for i in range(5):
    print(i)
break, continue, pass Ohjaavat silmukan kulkua:

break lopettaa silmukan

continue hyppää seuraavaan kierrokseen

pass tekee ei mitään (paikanvaraaja)

🧰 Tietorakenteet
Lista (list) Muokattava kokoelma:

python
ostoslista = ["maito", "leipä", "juusto"]
Sanakirja (dict) Avain-arvo -pareja:

python
henkilo = {"nimi": "Antti", "ika": 30}
Monikko (tuple) Muuttumaton lista:

python
koordinaatit = (60.2, 24.9)
Joukko (set) Unikkeja arvoja:

python
numerot = {1, 2, 3}
🧱 Rakenteet ja laajennukset
Moduuli Python-tiedosto, joka sisältää koodia. Voidaan tuoda toiseen tiedostoon import-komennolla.

Kirjasto (library) Kokoelma moduuleja, esim. math, random, datetime.

Paketti (package) Moduulien kansiorakenne, jossa on __init__.py-tiedosto.

Luokka (class) Määrittelee olion rakenteen ja toiminnan:

python
class Auto:
    def __init__(self, merkki):
        self.merkki = merkki
🧪 Erikoistoiminnot
Poikkeusten käsittely (try, except) Estää virhetilanteiden kaatumisen:

python
try:
    jako = 10 / 0
except ZeroDivisionError:
    print("Ei voi jakaa nollalla")
List comprehension Lyhyt tapa luoda listoja:

python
neliot = [x**2 for x in range(10)]
Lambda-funktio Nimettömiä funktioita:

python
summa = lambda x, y: x + y