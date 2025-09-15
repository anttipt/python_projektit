import requests

def hae_saa(kaupunki, api_avain):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}&units=metric&lang=fi"
    vastaus = requests.get(url)

    if vastaus.status_code == 200:
        data = vastaus.json()
        nimi = data['name']
        lampotila = data['main']['temp']
        kuvaus = data['weather'][0]['description']
        tuuli = data['wind']['speed']
        print(f"\n🌤️ Sää kohteessa {nimi}:")
        print(f"  Lämpötila: {lampotila}°C")
        print(f"  Kuvaus: {kuvaus}")
        print(f"  Tuulen nopeus: {tuuli} m/s\n")
    else:
        print("❌ Kaupunkia ei löytynyt tai API-avain on virheellinen.")

def main():
    print("=== Sääsovellus ===")
    api_avain = input("Syötä OpenWeatherMap API-avain: ")
    kaupunki = input("Syötä kaupunki: ")
    hae_saa(kaupunki, api_avain)

if __name__ == "__main__":
    main()
