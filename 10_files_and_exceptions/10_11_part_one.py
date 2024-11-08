# Challenge level 8/10
import json

# Prompt the user for their favorite number
favorite_number = input("What is your favorite number? ")

# Convert the input to an integer
favorite_number = int(favorite_number)

# Store the favorite number in a JSON file
with open('favorite_number.json', 'w') as f:
    json.dump(favorite_number, f)

print("Your favorite number has been saved!")