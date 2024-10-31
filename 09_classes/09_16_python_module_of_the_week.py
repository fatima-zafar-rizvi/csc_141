import random

# Generate a random float
print(random.random())

# Generate a random integer between 1 and 10
print(random.randint(1, 10))

# Randomly select an element from a list
items = ['apple', 'banana', 'cherry']
print(random.choice(items))

# Shuffle a list
deck = ['Ace', 'King', 'Queen', 'Jack']
random.shuffle(deck)
print(random.choice(deck))

# Set a seed for reproducibility
random.seed(42)
print(random.random())