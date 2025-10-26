```# Import OS module
import os

# User input section
folder = input("Pick the folder name")
file = input("Which file in the folder?")

# Define {path} with .exists to check if available
path = os.path.join(folder, file)

# IF the os.path.exists for {path} then print true otherwise false.
if os.path.exists(path):
    print(f"True! {path}")
else:
    print(f"False! {path}")```
