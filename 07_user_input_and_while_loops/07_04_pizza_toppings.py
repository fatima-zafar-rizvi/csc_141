
# Using while loop with user input.
# And letting the user choose when to quit.
message = "\nWhat kind of toppings would you like on your pizza? "
message += "\nEnter 'quit' to stop."

toppings = ""
while toppings != 'quit':
    toppings = input(message)

    if toppings != 'quit':
        print(f"\nWe have added {toppings} to your pizza.")