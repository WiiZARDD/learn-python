# This is version one of Twitter/X Checker
# Simple script to check availability of username on X/Twitter
# https://github.com/WiiZARDD

import requests
import time
import os

banner = r"""
╔══════════════════════════════════════════════╗
║      X / TWITTER USERNAME INTEL CONSOLE      ║
╠══════════════════════════════════════════════╣
║  • Check if a username is available          ║
║  • See if it's taken / banned / available    ║
║  • Data pulled live from api.twitter.com     ║
╠══════════════════════════════════════════════╣
║     Made by: https://github.com/WiiZARDD     ║
╚══════════════════════════════════════════════╝
"""

main = r"""
[+] Pick a username to look up on X/Twitter

    Examples:
        ├─ elonmusk
        ├─ jack
        └─ tester   (reserved / banned word)
"""

def Clear():
    os.system('cls' if os.name == "nt" else 'clear')

# --> Print all data after user input
def lookup(data):
    print(" ")
    if data['valid'] is False:
        if data['reason'] == "invalid_username":
            print(f"Invalid: {data['msg']}")
        elif data['reason'] == "is_banned_word":
            print("This word is banned")
        else:
            print(f"{data['msg']}")
    else:
        print(f"{data['msg']}")
    time.sleep(0.3)
    input("Press any key to return to the menu...")
    Clear()
    menu()

def menu():
    Clear()
    print(banner)
    print(main)
    u = input('''
    Pick a username to lookup: 

    ''')
    r = requests.get(f"https://api.twitter.com/i/users/username_available.json?username={u}", headers={"User-Agent": "Mozilla/5.0"})
    data = r.json() # Convert the data to JSON for Python
    lookup(data)

menu()
