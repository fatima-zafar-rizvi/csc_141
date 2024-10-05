# Everyone's favorite numbers:
favorite_numbers = {
    'Alice': [7, 14, 21],
    'Bob': [3, 8, 15],
    'Charlie': [10, 22, 35]
}

# Loop through the dictionary and print each person's favorite numbers
for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are:")
    for number in numbers:
        print(f" - {number}")
    print()