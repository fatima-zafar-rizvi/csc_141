# Using dictionary to store information about a person:
spiderman = {
    'first_name': 'peter', 
    'last_name': 'parker', 
    'age': '19', 
    'city': 'nyc'
    }

antman = {
    'first_name': 'scott', 
    'last_name': 'lang', 
    'age': '46', 
    'city': 'san francisco'
    }

deadpool = {
    'first_name': 'wade', 
    'last_name': 'wilson', 
    'age': '35', 
    'city': 'vancouver'
    }

# Using list to hold dictionaries:
people = [spiderman, antman, deadpool]

for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()