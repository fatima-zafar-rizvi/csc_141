# Dictionary of rivers and where they are located:
rivers = {'Ganges river': 'India', 'Mississippi river': 'America', 
          'Amazon river': 'Brazil', 'Yellow river': 'China', 
          'Nile river': 'Egypt'}

# Use loop to print keys and their values:
for river, country in rivers.items():
    print(f"The {river} is located in {country}.")

# Use loop to print keys:
print(f"\nHere is the list of different rivers in the world:")
for river in rivers.keys():
    print(river)

# Use loop to print values:
print(f'\nHere is the list of locations where there are famous'
      'rivers in the world:')
for country in rivers.values():
    print(country)