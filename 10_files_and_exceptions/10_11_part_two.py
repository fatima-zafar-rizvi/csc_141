# Challenge level 8/10
import json

# Read the favorite number from the JSON file
try:
    with open('favorite_number.json', 'r') as f:
        favorite_number = json.load(f)
    
    # Print the message with the user's favorite number
    print(f"I know your favorite number! It's {favorite_number}.")
except FileNotFoundError:
    print("Sorry, the file with your favorite number is missing.")
