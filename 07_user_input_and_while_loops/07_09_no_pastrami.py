
# List of sandwich orders, including 'pastrami' three times:
sandwich_orders = ['tuna', 'turkey', 'ham', 'pastrami', 'veggie', 'pastrami', 'club', 'pastrami']
# Empty list for finished sandwiches:
finished_sandwiches = []

# Print message about pastrami being unavailable:
print("The deli has run out of pastrami sandwiches.")

# Remove all occurrences of 'pastrami' using a while loop:
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Loop through each sandwich order:
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    # Move the sandwich to the finished sandwiches list:
    finished_sandwiches.append(sandwich)

# Print a message listing all finished sandwiches:
print("\nAll sandwiches have been made:")
for finished in finished_sandwiches:
    print(f"- {finished} sandwich")