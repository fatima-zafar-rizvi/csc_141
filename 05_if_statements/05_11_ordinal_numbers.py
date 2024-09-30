# List of numbers from 1 to 9
numbers = list(range(1, 10))

# Loop through the list and determine the ordinal suffix
for number in numbers:
    if number == 1:
        suffix = 'st'
    elif number == 2:
        suffix = 'nd'
    elif number == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    
    # Print the ordinal number
    print(f"{number}{suffix}")