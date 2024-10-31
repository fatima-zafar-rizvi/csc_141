import random

# Define the winning ticket
winning_ticket = {1, 23, 34, 45, 12, 6}  # Example winning numbers
my_ticket = set()  # Initialize my_ticket as an empty set

# Counter for the number of attempts
attempts = 0

# Loop until my_ticket matches the winning_ticket
while my_ticket != winning_ticket:
    my_ticket = set(random.sample(range(1, 50), 6))  # Generate a random ticket
    attempts += 1  # Increment the attempts counter

# Print the result
print(f"It took {attempts} attempts to win the lottery with the ticket: "
      f"{winning_ticket}.")
