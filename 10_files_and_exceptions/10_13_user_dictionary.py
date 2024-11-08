# Challenge level 8/10

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

def get_new_user_info(path):
    # Prompt for new user information.
    username = input("What is your name? ")
    age = input("How old are you? ")
    favorite_color = input("What is your favorite color? ")
    
    # Store the information in a dictionary
    user_info = {
        "username": username,
        "age": age,
        "favorite_color": favorite_color
    }

    # Write the dictionary to a file in JSON format
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info

def greet_user():
    # Greet the user with their information.
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)
    
    if user_info:
        # If the information is already stored, greet the user 
        print(f"Welcome back, {user_info['username']}!")
        print(f"We remember that you are {user_info['age']} years old and "
              f"your favorite color is {user_info['favorite_color']}.")
    else:
        # Collect new user information if not already stored
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, "
              f"{user_info['username']}!")

greet_user()