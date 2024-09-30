# List of current usernames
current_users = ['timo', 'xavier', 'federico', 'gusto', 'gerardo']

# List of new usernames
new_users = ['Alix', 'xavier', 'federico', 'angela', 'Tami']

# Create a lowercase version of the current_users list for comparison
lowercase_current_users = [user.lower() for user in current_users]

# Check for uniqueness of new usernames
for new_user in new_users:
    if new_user.lower() in lowercase_current_users:
        print(f"The username '{new_user}' has already been used. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")