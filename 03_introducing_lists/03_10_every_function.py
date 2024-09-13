
'''
Everthing I have learnt in Chapter 3.
'''

# Creating a list:
formula_1 = ['redbull', 'mercedes', 'ferrari', 'mclaren', 'williams']
print(formula_1)

# Accessing elements in list:
print(formula_1[0])
print(formula_1[1].title())

# Using individual values from list:
message = f"\nMy favorite Formula 1 team is {formula_1[2].title()}.\n"
print(message)

# Modifying elements in list:
formula_1[0] = 'haas'
print(formula_1)

# Appending elements to the end of a list:
formula_1.append('redbull')
print(formula_1)

# Inserting elements into list:
formula_1.insert(3, 'alpine')
print(formula_1)

# Removing an element:
del formula_1[3]
print(formula_1)

popped_formula_1 = formula_1.pop(0)
print(formula_1)
print(popped_formula_1)

formula_1.remove('williams')
print(formula_1)

# Sorting list permanently with sort() method:
formula_1.sort()
print(formula_1)

formula_1.sort(reverse=True)
print(formula_1)

# Sorting list temporarily with sort() function:
# Originla list-
print(formula_1)
print(sorted(formula_1))
print(formula_1)

# Print list with reverse() method:
print(formula_1)
formula_1.reverse()
print(formula_1)

# Finding the length of the list:
print(len(formula_1))
