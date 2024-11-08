# Challenge level 8/10
# Modify the combined the two codes from 10-11

import json
from pathlib import Path

# Define the file path using Path from pathlib
file_path = Path('favorite_number.json')

# Prompt the user for their favorite number
favorite_number_input = input("What is your favorite number? ")

# Convert the input to an integer
favorite_number_input = int(favorite_number_input)

# Check if the file exists
if file_path.exists():
    try:
        # Read the favorite number from the JSON file
        with open(file_path, 'r') as f:
            stored_favorite_number = json.load(f)

        # Compare the stored favorite number with the input number
        if stored_favorite_number == favorite_number_input:
            print(f"I knew your favorite number was {stored_favorite_number}!")
        else:
            # If the number is different, update the stored number
            with open(file_path, 'w') as f:
                json.dump(favorite_number_input, f)
            print(f"I didn't know that! Let me remember that for next time.")

    except FileNotFoundError:
        print("Sorry, the file with your favorite number is missing.")
else:
    # If the file doesn't exist, store the favorite number
    with open(file_path, 'w') as f:
        json.dump(favorite_number_input, f)
    print("Your favorite number has been saved!")