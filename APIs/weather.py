import os
import sys
import time
import requests

key = "Your API Key"
url = f"https://api.weatherapi.com/v1/forecast.json?key={key}"

def Clear():
    os.system('cls' if os.name == "nt" else 'clear')

def spin():
    spinner = ['/', '-', '|', '\\']
    for i in range(5):
        sys.stdout.write("\r Validating API Key... " + spinner[i % len(spinner)])
        sys.stdout.flush()
        time.sleep(0.2)

def weather(url, zipcode):
    data = requests.get(url).json()
    print(f"Location: {data['location']['name']} " + f'[{zipcode}]')
    print(f"Current temp: {data['current']['temp_f']}")
    print(f"Wind Direction: {data['current']['wind_dir']}")
    print(f"Forecast: {data['forecast']['forecastday'][0]['day']['condition']['text']}")
    print(" ")
    if data['forecast']['forecastday'][0]['day']['daily_will_it_rain'] == 0:
        print("Rain: (NONE)")
    else:
        print("Rain: (LIKELY)")
    if data['forecast']['forecastday'][0]['day']['daily_will_it_snow'] == 0:
        print("Snow: (NONE)")
    else:
        print("Snow: (LIKELY)")
    print(" ")
    print(f"Sunrise: {data['forecast']['forecastday'][0]['astro']['sunrise']}")
    print(f"Sunset: {data['forecast']['forecastday'][0]['astro']['sunset']}")
    print(f"Moonrise: {data['forecast']['forecastday'][0]['astro']['moonrise']}")
    print(f"Moonset: {data['forecast']['forecastday'][0]['astro']['moonset']}")
    if data['forecast']['forecastday'][0]['astro']['is_moon_up'] == 0:
        print("Moon: DOWN")
    else:
        print("Moon: UP")
    if data['forecast']['forecastday'][0]['astro']['is_sun_up'] == 0:
        print("Sun: DOWN")
    else:
        print("Sun: UP")
    print(" ")
    main = input("Press any key to return to the menu...")
    Clear()
    menu()

def menu():
    Clear()
    userInput = input("Pick a zipcode: ")
    if userInput.isdigit():
        if len(userInput) == 5:
            zipcode = userInput
            url = f"https://api.weatherapi.com/v1/forecast.json?key={key}&q={zipcode}&days=1&aqi=no&alerts=no"
            print(" ")
            spin()
            time.sleep(2)
            Clear()
            weather(url, zipcode)
        else:
            print("Must be 5 digits!")
    else:
        print("Must be digits!")

menu()
