# 📝 To-do CLI - Pythonilla

Komentorivipohjainen tehtävienhallintasovellus, jossa käyttäjä voi lisätä, poistaa ja merkitä tehtäviä tehdyiksi. 
Tehtävät tallennetaan pysyvästi JSON-tiedostoon. Sovellus tukee myös deadlineja ja prioriteetteja.

---

## 🔧 Ominaisuudet

- ✅ Tehtävän lisääminen
- ❌ Tehtävän poistaminen
- ☑️ Tehtävän merkitseminen tehdyksi
- 📄 Tehtävien listaus
- 📅 Deadline-tuki (`YYYY-MM-DD`)
- 🔥 Prioriteettituki (`low`, `medium`, `high`)
- 💾 Tallennus `tasks.json`-tiedostoon

---

## 🖥️ Käyttöohjeet

Komentoriviltä:

```bash
python todo.py
```

Sovelluksessa käytettävät komennot:

```
list                 - Näytä kaikki tehtävät
add <otsikko> | <deadline> | <prioriteetti>
                     - Lisää uusi tehtävä
						Esim: add Kirjoita README | 2025-10-31 | high
del <numero>         - Poista tehtävä
done <numero>        - Merkitse tehtävä tehdyksi
exit                 - Poistu sovelluksesta
```


## 📦 Tallennusmuoto (JSON)

```
{
  "title": "Kirjoita README",
  "done": false,
  "deadline": "2025-10-31",
  "priority": "high"
}
```

## 🧪 Esimerkki
```
>> add Kirjoita README | 2025-10-31 | high
>> list
1. [✘] Kirjoita README | Deadline: 2025-10-31 | Prioriteetti: high
>> done 1
>> list
1. [✔] Kirjoita README | Deadline: 2025-10-31 | Prioriteetti: high
```

## 📁 Tiedostorakenne
```
todo_cli/
├── todo.py         # Sovelluksen logiikka
├── tasks.json      # Tallennustiedosto
```

## 💡 Ideoita jatkokehitykseen

🔔 Deadline-ilmoitukset

📊 Tehtävien järjestäminen deadlinen tai prioriteetin mukaan

🧪 Testit unittest-moduulilla

🌐 Versio web-käyttöliittymällä (React + Flask)



