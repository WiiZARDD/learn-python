# Import modules for FakeName Script
# --> Requests for communicating with internet via machine to pull data
import requests
import os

# Very simple Clear prompt function
# If OS name is "New Technology" (Microsoft) -> Run 'cls'
# Otherwise, run 'clear' (Linux, Ubuntu, Mac OSX)
def Clear():
    os.system('cls' if os.name == "nt" else 'clear')

# FakeName Function -> Displays generated data via API call
# API Used: https://randomuser.me/api (RandomUser.me)
def fakeName(gender, url):
    data = requests.get(url).json()
    # Loop is currently useless but harmless, will add use for loop in future...
    # Purpose of for loop: To practice 
    for i in range(1):
        print(data["results"][0]["name"]["first"] + " " + data["results"][0]["name"]["last"] + " " + f'[{data["results"][0]["name"]["title"]}]')
        fakeGender = data["results"][0]["gender"]
        fakeGender_first = fakeGender[0].upper()
        fakeGender_rest = fakeGender[1:len(fakeGender)]
        # All FakeName information (Gender, Location, City, State, Country, more coming soon...)
        print("Gender: " + fakeGender_first + fakeGender_rest)
        print("Location: " + str(data['results'][0]['location']['street']['number']) + " " + data["results"][0]["location"]["street"]["name"])
        print("City: " + data["results"][0]["location"]["city"])
        print("State: " + data["results"][0]["location"]["state"])
        print("Country: " + data["results"][0]["location"]["country"])
        print(" ")
        # Return to menu option -->
        menu = input("Would you like to return to the menu? (Y/N): ")
        if menu.lower().startswith("y"):
            Clear()
            nameGen()
        elif menu.lower().startswith("n"):
            print("Closing application...")
            confirmation = input("Press any key to confirm...")
            break

# Name generator function
# Allows user to select gender, creates API call, confirms selection
# Sends API call to fakeName() function to fetch data for selected gender
def nameGen():
    gender = None
    url = "https://randomuser.me/api"
    userInput = input("Choose a gender (Male or Female): ")
    if userInput.lower().startswith("m"):
        gender = "male"
        url = f"https://randomuser.me/api?gender={gender}"
        data = requests.get(url).json()
        print("Gender set to: " + data['results'][0]['gender'])
        print(" ")
        proceed = input("Ready to proceed? [PRESS ANY KEY]")
        Clear()
        fakeName(gender, url)
    elif userInput.lower().startswith("f"):
        gender = "female"
        url = f"https://randomuser.me/api?gender={gender}"
        data = requests.get(url).json()
        print(f"Gender set to: {data['results'][0]['gender']}")
        print(" ")
        proceed = input("Ready to proceed? [PRESS ANY KEY]")
        Clear()
        fakeName(gender, url)

# Begin nameGen() function --> Starts Fake Name script
nameGen()
