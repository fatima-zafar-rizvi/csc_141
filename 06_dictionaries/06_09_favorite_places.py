# Putting everyone's favortie places in a dictionary.
# Also, values are a list containing strings.
favorite_places = {
    'Alice': ['Paris', 'Tokyo', 'New York'],
    'Bob': ['London', 'Berlin'],
    'Charlie': ['Sydney', 'Barcelona', 'Rio de Janeiro']
}

# Loop through the dictionary and print each person's favorite places
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f" - {place}")
    print()  