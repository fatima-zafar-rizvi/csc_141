
# Exercise 04_01:
pizzas = ['Cheese pizza', 'Buffalo chicken pizza', 'Chicken fajita pizza']

for pizza in pizzas:
    print(pizza)
    print(f"\n I like {pizza.title()}.\n")
print("\nI really love pizza!\n")

# Exercise 04_05:
digits = list(range(1, 1000001))

print(min(digits))
print(max(digits))
print(sum(digits))

# Exercise 04_10:
cubes = [value**3 for value in range(1, 11)]

print(cubes)
print("\nThe first three items in the list are: " + str(cubes[:3]))
print("\nThree items from the middle of the list are: " + str(cubes[3:6]))
print("\nThe last three items in the list are: " + str(cubes[7:]))