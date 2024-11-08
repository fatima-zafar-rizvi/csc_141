# Challenge level 9/10
from pathlib import Path
import json

def get_stored_user_info(path):
    # Get stored user information if available.
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info():
    # Prompt for new user information.
    username = input("What is your name? ")
    age = input("How old are you? ")
    favorite_color = input("What is your favorite color? ")
    
    # Store the information in a dictionary
    return {
        "username": username,
        "age": age,
        "favorite_color": favorite_color
    }

def save_user_info(path, user_info):
    # Write the dictionary to a file in JSON format
    contents = json.dumps(user_info)
    path.write_text(contents)

def greet_user():
    path = Path('user_info.json')
    stored_info = get_stored_user_info(path)
    
    if stored_info:
        # Confirm if this is the correct user
        is_correct_user = input(f"Is this you, {stored_info['username']}? "
                                "(yes/no): ").strip().lower()
        if is_correct_user == 'yes':
            print(f"Welcome back, {stored_info['username']}!")
            print(f"We remember that you are {stored_info['age']} years old "
                  f"and your favorite color is "
                  f"{stored_info['favorite_color']}.")
        else:
            # Get new user information if it's a different user
            print("Let's get your information.")
            new_info = get_new_user_info()
            save_user_info(path, new_info)
            print(f"We'll remember you when you come back, "
                  f"{new_info['username']}!")
    else:
        # Save new information if no stored info exists
        new_info = get_new_user_info()
        save_user_info(path, new_info)
        print(f"We'll remember you when you come back, "
              f"{new_info['username']}!")

greet_user()