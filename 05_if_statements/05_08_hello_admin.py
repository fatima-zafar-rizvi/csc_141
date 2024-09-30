
# List of usernames:
usernames = ['admin', 'bob-123', 'fatima_01', 'ali.013', 'smelly_cat']

for username in usernames:
    if username == 'admin':
        print("\nHello admin, would you like to see a status report?")
    else:
        print(f"\nHello {username}, thank you for logging in again.")