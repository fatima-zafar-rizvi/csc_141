
# List comprehension 04_09:
cubes = [value**3 for value in range(1, 11)]
print(cubes)

# Exercise 04_10:
print("\nThe first three items in the list are: " + str(cubes[:3]))

print("\nThree items from the middle of the list are: " + str(cubes[3:6]))

print("\nThe last three items in the list are: " + str(cubes[7:]))