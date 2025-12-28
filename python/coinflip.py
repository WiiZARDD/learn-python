# Coinflip Time Complexity (Big O Notation): O(n)
# GITHUB: https://github.com/WiiZARDD
# Python fundamentals - Coinflip script

# Import modules
import os
import random
import sys
import time

# Possible to land on: Heads or Tails
coin = ["heads", "tails"]
# Spinner / Loading animation
animation = ['/', '-', '|', '\\']

# Function to clear CLI using clear()
def clear():
    # If OS Name is "New Technology" (Windows)
    # then run 'cls' to clear CLI
    if os.name == "nt":
        os.system('cls')
    # Otherwise, use 'clear' if OS is Linux, Mac OS, etc...
    else:
        os.system("clear")

# Coinflip function
# FEATURES:
# - Pick amount of coinflips
# - Coinflipping animation / Loading animation
# - Returns result for each flip
# - Only accepts int input otherwise will reject coinflip

def coinflip(amount):
    # Begin coinflip loop for (amount)
    for coinflip in range(amount):
        print(f"\nFlipping coin! #{coinflip+1}")
        # Initiate coinflip animation / loading loop
        for spin in range(4):
            sys.stdout.write("\r" + animation[spin % len(animation)])
            sys.stdout.flush()
            time.sleep(0.1)
            result = random.choice(coin)
        # Ensure CLI clears animation before printing result
        sys.stdout.write("\r    ")
        sys.stdout.flush()

        # Final coinflip result
        print(f"\n{result}")

# Ask user how many times they would like to coinflip
print("How many times would you like to flip the coin?")
choice = input("")
# If user inputs a digit, convert to int to be safe, then begin coinflip function
if choice.isdigit():
    amount = int(choice)
    print("Success!")
    coinflip(amount)
# Otherwise, tell the user they have entered an invalid choice (Letters for instance...)
else:
    print("Not a valid choice!")
