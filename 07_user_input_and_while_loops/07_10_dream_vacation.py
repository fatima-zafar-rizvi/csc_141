
# Initialize an empty dictionary to store responses:
vacation_polls = {}

# Function to poll users:
def poll_users():
    while True:
        name = input("What is your name? (or type 'quit' to finish): ")
        if name.lower() == 'quit':
            break
        destination = input("If you could visit one place in the world, where "
                            "would you go? ")
        vacation_polls[name] = destination

# Call the function to start polling:
poll_users()

# Print the results of the poll:
print("\n--- Vacation Poll Results ---")
for name, destination in vacation_polls.items():
    print(f"{name} would like to visit {destination}.")