
# Using the modulo Operator (%) which divides one number by another and returns
# the remainder:
number = input("Choose a number: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number is {number} is a multiple of ten.")
else:
    print(f"\nThe number is {number} is not a multiple of ten.")