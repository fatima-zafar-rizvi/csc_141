
# Places I want to visit:
places = ['south korea', 'japan', 'indonesia', 'switzerland', 'iceland']
print(places)

# Temporary alphabetical order list:
print("\nHere is the alphabetical order list:")
print(sorted(places))
print(places)

# Temporary reverse-alphabetical order list:
print("\nHere is the reverse-alphabetical order list:")
print(sorted(places, reverse=True))
print(places)

# Reverse change to the order of the list:
print("\nHere is the reverse order of the list:")
places.reverse()
print(places)

# Original order of the list:
print("\nHere is the original order of the list:")
places.reverse()
print(places)

# Sorting list permanently to alphabetical order:
print("\nHere is the sorted list:")
places.sort()
print(places)

# Sorting list permanently to reverse-alphabetical order:
print("\nHere is the reverse sorted list:")
places.sort(reverse=True)
print(places)