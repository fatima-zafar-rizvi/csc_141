# Challenge level 6/10

from pathlib import Path

#Define path for guest_book.txt
path = Path('guest_book.txt')
print("Enter 'quit' to stop entering names.\n")

# Using while loop
while True:
    name = input("Please enter your name: ")
    if name.lower() == 'quit':
        break
    else:
        # Each entry appears on a new line
        with path.open(mode='a') as file:
            file.write(name + "\n")
        print("You are now added to the guest book!")