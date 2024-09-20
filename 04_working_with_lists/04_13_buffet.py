
# Five basic foods at a restaurant:
restaurant = ('breadsticks', 'pasta', 'salad', 'pizza', 'fries')
print("\n\t Our restaurant's buffet-style menu includes:\n")
for original in restaurant:
    print("\n\t" + str(original))

# Type Error:
# restaurant[0] = ('burgers')

# Modify the tuple:
restaurant = ('burgers', 'pasta', 'hotdogs', 'pizza', 'fries')
print("\n\t We ran out of a few menu items so here is the revised menu of the day:\n")
for modified in restaurant:
    print("\n\t" + str(modified))