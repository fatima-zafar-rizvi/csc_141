
# Putting two of the programs from Foods.py into a for loop:

potluck_list = ['pizza', 'falafel', 'carrot cake', 'cannoli']

print("\t I am hosting a potluck this weekend please bring the following:\n")

for dishes in potluck_list:
    print(dishes)

replaced_potluck = potluck_list[:]
replaced_potluck.append('ice cream')
print("\n\t I forgot to add a dish on the potluck list. Here is the new list:\n")

for replace in replaced_potluck:
    print(replace)