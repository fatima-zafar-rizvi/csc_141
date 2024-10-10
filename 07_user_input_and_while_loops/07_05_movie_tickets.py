
# Using while loop with if statements:
while True:
    age_input = input("Please enter your age (or 'quit' to exit): ")
    
    if age_input.lower() == 'quit':
        print("Thank you! Goodbye.")
        break
    
    try:
        age = int(age_input)

        if age < 3:
            print("Your ticket is free!")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
    except ValueError:
        print("Invalid input. Please enter a valid age or 'quit' to exit.")