## Asennetaan requests-kirjasto http-pyyntöjen tekemiseen ja verkkopalvelimien vastausten käsittelyyn
import requests # Tuodaan käyttöön requests-kirjasto, jolla voidaan tehdä HTTP-pyyntöjä

# Määritellään funktio, joka hakee säätiedot annetulle kaupungille ja API-avaimella
def hae_saa(kaupunki, api_avain):
    # Rakennetaan URL OpenWeatherMapin rajapintaan, mukaan lukien kaupunki, API-avain, yksiköt ja kieli
    url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}&units=metric&lang=fi"
    # Lähetetään GET-pyyntö URL-osoitteeseen
    vastaus = requests.get(url)

    # Tarkistetaan, onnistuiko pyyntö (statuskoodi 200 tarkoittaa OK)
    if vastaus.status_code == 200:
        data = vastaus.json() # Muutetaan vastaus JSON-muotoon (Pythonin sanakirjaksi)
        # Poimitaan tarvittavat tiedot JSON-rakenteesta
        nimi = data['name'] # kaupungin nimi
        lampotila = data['main']['temp'] # lämpötila celcius-asteina
        kuvaus = data['weather'][0]['description'] # sääkuvaus (esim. selkeää)
        tuuli = data['wind']['speed'] # tuulen nopeus m/s
        # Tulostetaan säätiedot käyttäjälle
        print(f"\n🌤️ Sää kohteessa {nimi}:")
        print(f"  Lämpötila: {lampotila}°C")
        print(f"  Kuvaus: {kuvaus}")
        print(f"  Tuulen nopeus: {tuuli} m/s\n")
    else:
        # Jos pyyntö epäonnistui, ilmoitetaan virheestä
        print("❌ Kaupunkia ei löytynyt tai API-avain on virheellinen.")
# Pääfunktio, joka pyytää käyttäjältä tarvittavat tiedot ja kutsuu sääfunktion
def main():
    print("=== Sääsovellus ===")
    api_avain = input("Syötä OpenWeatherMap API-avain: ") # Käyttäjä syöttää API-avaimen
    kaupunki = input("Syötä kaupunki: ") # käyttäjä syöttää kaupungin nimen
    hae_saa(kaupunki, api_avain) # Kutsutaan sääfunktiota annetuilla tiedoilla

# Tarkistetaan, onko tiedosto suoraan ajossa (eikä esim. tuotu moduulina)
if __name__ == "__main__":
    main() # Suoritetaan pääfunktio
