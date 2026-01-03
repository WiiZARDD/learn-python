# Import modules
import os
import sys
import time
import requests

# Get FREE API Key here -> https://www.weatherapi.com/
key = "Your API Key"
url = f"https://api.weatherapi.com/v1/forecast.json?key={key}"

# Standard/Universal clear function
def Clear():
    os.system('cls' if os.name == "nt" else 'clear')

# Spinner / Loading animation
def spin():
    # Array for each character to make up spinner animation
    spinner = ['/', '-', '|', '\\']
    # Begin loop each character in spinner[length(spinner)]
    # Creates loading animation
    for i in range(5):
        sys.stdout.write("\r Validating API Key... " + spinner[i % len(spinner)])
        sys.stdout.flush()
        time.sleep(0.2)

# Weather function -> Fetchs data via API Call
# Outputs real time weather analysis of zipcode
def weather(url, zipcode):
    # Fetch data from URL, put it into JSON format for Python
    # Thankfully, WeatherAPI already provides in JSON format
    data = requests.get(url).json()
    print(f"Location: {data['location']['name']} " + f'[{zipcode}]')
    print(f"Current temp: {data['current']['temp_f']}")
    print(f"Wind Direction: {data['current']['wind_dir']}")
    print(f"Forecast: {data['forecast']['forecastday'][0]['day']['condition']['text']}")
    print(" ")
    # Check if it will rain
    if data['forecast']['forecastday'][0]['day']['daily_will_it_rain'] == 0:
        print("Rain: (NONE)")
    else:
        print("Rain: (LIKELY)")
    # Check if it will snow
    if data['forecast']['forecastday'][0]['day']['daily_will_it_snow'] == 0:
        print("Snow: (NONE)")
    else:
        print("Snow: (LIKELY)")
    print(" ")
    # Astro forecast, sunrise, sunset, etc...
    print(f"Sunrise: {data['forecast']['forecastday'][0]['astro']['sunrise']}")
    print(f"Sunset: {data['forecast']['forecastday'][0]['astro']['sunset']}")
    print(f"Moonrise: {data['forecast']['forecastday'][0]['astro']['moonrise']}")
    print(f"Moonset: {data['forecast']['forecastday'][0]['astro']['moonset']}")
    # Check if moon is UP or DOWN
    if data['forecast']['forecastday'][0]['astro']['is_moon_up'] == 0:
        print("Moon: DOWN")
    else:
        print("Moon: UP")
    # Check if sun is UP or DOWN
    if data['forecast']['forecastday'][0]['astro']['is_sun_up'] == 0:
        print("Sun: DOWN")
    else:
        print("Sun: UP")
    print(" ")
    # Initiate return to menu prompt
    main = input("Press any key to return to the menu...")
    Clear()
    return

# Main menu function
# Allows user to input zipcode -> This will be used in API call to fetch real time data
def menu():
    Clear()
    # Allow user to input zipcode
    userInput = input("Pick a zipcode: ")
    # Check if input is digits
    if userInput.isdigit():
        # If input is digits, confirm input length is 5 digits
        if len(userInput) == 5:
            # If input length is 5 digits, set input to {zipcode}
            zipcode = userInput
            url = f"https://api.weatherapi.com/v1/forecast.json?key={key}&q={zipcode}&days=1&aqi=no&alerts=no"
            print(" ")
            spin()
            time.sleep(2)
            Clear()
            weather(url, zipcode)
        # Otherwise, input must be 5 digits to fulfill zipcode requirements
        else:
            print("Must be 5 digits!")
    # Otherwise, input must be digits
    else:
        print("Must be digits!")

# Begin the main script
#menu()

# Prevent stack buildup...
if __name__ == __main__:
    while True:
        menu()
