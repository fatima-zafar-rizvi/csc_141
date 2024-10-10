
# Using the int() to accept numerical user input: 
seating = input("How many people are there in your dinner group? ")
seating = int(seating)

# Using if and else statements to print messages based on user inputs:
if seating > 8:
    print("\nMy apologies! You will have to wait for a table.")
else:
    print("\nYour table is ready!")