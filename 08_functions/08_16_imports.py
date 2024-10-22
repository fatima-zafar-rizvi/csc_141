
# main.py

# Importing the function in various ways
import greetings
from greetings import greet_user
from greetings import greet_user as greet
import greetings as g
from greetings import *

# Using the different import methods
greet_user("Alice")        # Using direct import
greet("Bob")               # Using alias
greetings.greet_user("Eve")  # Using import module_name
g.greet_user("Charlie")    # Using import module_name as mn
greet_user("David")        # Using from module_name import *
