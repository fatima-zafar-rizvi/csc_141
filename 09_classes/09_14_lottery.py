import random

# Create a list containing 10 numbers and 5 letters
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select 4 items from the list
winning_selection = random.sample(items, 4)

# Print the winning message
print(f"Congratulations! Any ticket matching these 4 numbers or "
      f"letters: {winning_selection} wins a prize!")
