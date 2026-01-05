# Check to see if a github username is available
# Check github user via Github API -> https://api.github.com/users/{u}
# Created by: https://github.com/WiiZARDD

import requests
import time
import os

def Clear():
    os.system('cls' if os.name == "nt" else 'clear')

def lookup(data):
    if data.get("message") == "Not Found":
        print("Username is available!")
    else:
        print("Username is taken...")
    mainmenu = input("Press any key to return to the menu...")
    main()

def main():
    Clear()
    u = input("Pick a username: ")
    url = f"https://api.github.com/users/{u}"
    data = requests.get(url).json()
    lookup(data)
    
main()
