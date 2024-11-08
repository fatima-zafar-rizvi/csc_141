# Challenge level 3/10

from pathlib import Path

# Prompt the user for their name
name = input("Please enter your name: ")

# Write the name in guest.txt
path = Path('guest.txt')
path.write_text(name)

print("You are now added to the guest list!")