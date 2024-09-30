# Test for equality:
magic_number = 27
print("\nThe magic number is 27.")
print(magic_number == 27) # True

print("\nThe magic number is 7.")
print(magic_number == 7)  # False

# Test for inequality:
dislike = 'oatmeal'
print("\nI know my friend likes spinach. So, that cannot be one of his dislikes.")
print(dislike != 'spinach') # True

print("\nMy friend dislikes fish.")
print(dislike == 'fish')  # False

# Test using the lower() method:
car = 'BMW'
print("\nI think my dad's favorite car is BMW.")
print(car.lower() == 'bmw') # True

print("\nI think my dad's favorite car is BMW.")
print(car == 'bmw')  # False

# Numerical test for equality:
class_grade = 98
print("\nI think I have a 98 in this class.")
print(class_grade == 98) # True

print("\nI think I have a 90 in this class.")
print(class_grade == 90)  # False

# Numerical test for inequality:
brother_age = 11
print("\nI keep forgetting my brother's age. I know he is not 10.")
print(brother_age != 10) # True

print("\nI keep forgetting my brother's age. I think he is 10.")
print(brother_age == 10) # False

# Numerical test for greater than:
cost_of_dress = 550
print("\nI am guessing that dress costs more than $500.")
print(cost_of_dress > 500) # True

print("\nI am guessing that dress costs more than $600.")
print(cost_of_dress > 600)  # False

# Numerical test for less than:
number_of_students = 20
print("\nThere are less than 30 students in my class.")
print(number_of_students < 30) # True

print("\nThere are less than 10 students in my class.")
print(number_of_students < 10)  # False

# Numerical test for greater than or equal to:
age = 20
print("\nIs age greater than or equal to 18?")
print(age >= 18)  # True

print("\nIs age greater than or equal to 21?")
print(age >= 21)  # False

# Numerical test for less than or equal to:
temperature = 75
print("\nIs temperature less than or equal to 80?")
print(temperature <= 80)  # True

print("\nIs temperature less than or equal to 70?")
print(temperature <= 70)  # False

# Test using 'and' keyword:
x = 5
print("\nIs x greater than 2 and less than 10?")
print(x > 2 and x < 10)  # True

print("\nIs x greater than 2 and less than 5?")
print(x > 2 and x < 5)  # False

# Test using 'or' keyword:
y = 3
print("\nIs y less than 5 or greater than 2?")
print(y < 5 or y > 2)  # True

print("\nIs y less than 2 or greater than 5?")
print(y < 2 or y > 5)  # False

# Test whether an item is in a list:
fruits = ['apple', 'banana', 'cherry']
print("\nIs 'banana' in the fruits list?")
print('banana' in fruits)  # True

print("\nIs 'orange' in the fruits list?")
print('orange' in fruits)  # False

# Test whether an item is not in a list:
vegetables = ['carrot', 'broccoli', 'spinach']
print("\nIs 'tomato' not in the vegetables list?")
print('tomato' not in vegetables)  # True

print("\nIs 'carrot' not in the vegetables list?")
print('carrot' not in vegetables)  # False