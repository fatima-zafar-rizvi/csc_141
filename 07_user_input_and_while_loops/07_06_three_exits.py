
# 07_04 Exercise:
message = "\nWhat kind of toppings would you like on your pizza? "
message += "\nEnter 'quit' to stop."

toppings = ""
while toppings != 'quit':
    toppings = input(message)

    if toppings != 'quit':
        print(f"\nWe have added {toppings} to your pizza.")

# Using conditional test in while statement:
message = "\nWhat kind of toppings would you like on your pizza? "
message += "\nEnter 'quit' to stop."

toppings = ""
while toppings != 'quit':
    toppings = input(message)

    if toppings != 'quit':
        print(f"\nWe have added {toppings} to your pizza.")

# Using active varible to control the loop:
message = "\nWhat kind of toppings would you like on your pizza? "
message += "\nEnter 'quit' to stop."

toppings = ""
continue_loop = True

while continue_loop:
    toppings = input(message)
    
    if toppings == 'quit':
        continue_loop = False
    else:
        print(f"\nWe have added {toppings} to your pizza.")

# Using a break statement to exit the loop:
message = "\nWhat kind of toppings would you like on your pizza? "
message += "\nEnter 'quit' to stop."

while True:
    toppings = input(message)
    
    if toppings == 'quit':
        break
    
    print(f"\nWe have added {toppings} to your pizza.")