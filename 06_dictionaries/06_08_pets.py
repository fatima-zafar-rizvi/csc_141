# Holding information about pets in dictionaries:
teddy = {
    'Animal': 'Dog',
    'Owner': 'Rob',
    'Breed': 'Golden Retriever',
    'Age': 3
}

mr_whiskers = {
    'Animal': 'Cat',
    'Owner': 'Alyssa',
    'Breed': 'Persian Flatnose',
    'Age': 7
}

toto = {
    'Animal': 'Parrot',
    'Owner': 'Kevin',
    'Breed': 'Macaw',
    'Age': 1
}

slytherin = {
    'Animal': 'Snake',
    'Owner': 'Eve',
    'Breed': 'Python',
    'Age': 5
}

ratatouille = {
    'Animal': 'Rat',
    'Owner': 'Peter',
    'Breed': 'Black Rat',
    'Age': 4
}

# Making list of the dictionaries:
pets = [teddy, mr_whiskers, toto, slytherin, ratatouille]

# Printing information using for loop:
for pet in pets:
    print(f"Owner: {pet['Owner']}")
    print(f"Animal: {pet['Animal']}")
    print(f"Breed: {pet['Breed']}")
    print(f"Age: {pet['Age']} years\n") 