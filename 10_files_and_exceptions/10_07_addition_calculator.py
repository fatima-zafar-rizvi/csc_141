# Challenge level 7/10:

'''Modify code from 10_06'''

def add_two_numbers():
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            
            # Add the numbers and print the result
            result = num1 + num2
            print(f"The result of adding {num1} and {num2} is: {result}")
            
            # Exit the loop if the operation is successful
            break
        
        except ValueError:
            # Handle the error if a non-numeric input is given
            print("Error: Please enter valid numbers only.")
            
# Call the function
add_two_numbers()