
# List of sandwich orders:
sandwich_orders = ['tuna', 'turkey', 'ham', 'veggie', 'club']
# Empty list for finished sandwiches:
finished_sandwiches = []

# Loop through each sandwich order:
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    # Move the sandwich to the finished sandwiches list:
    finished_sandwiches.append(sandwich)

# Print a message listing all finished sandwiches:
print("\nAll sandwiches have been made:")
for finished in finished_sandwiches:
    print(f"- {finished} sandwich")