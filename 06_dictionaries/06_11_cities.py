# Information of famous cities:
cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is known for its bustling streets and is the world’s most populous metropolitan area.'
    },
    'Paris': {
        'country': 'France',
        'population': 2140526,
        'fact': 'Paris is famous for its art, fashion, and the iconic Eiffel Tower.'
    },
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'New York City is known as "The Big Apple" and is home to Times Square and Central Park.'
    }
}

# Loop through the dictionary and print each city's information
for city, info in cities.items():
    print(f"{city}:")
    print(f" - Country: {info['country']}")
    print(f" - Population: {info['population']}")
    print(f" - Fact: {info['fact']}")
    print()  