# Information of famous cities:
cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'area': 2191,  # in square kilometers
        'currency': 'Yen',
        'famous_landmarks': ['Tokyo Tower', 'Shibuya Crossing', 
                             'Senso-ji Temple'],
        'fact': 'Tokyo is known for its bustling streets and is the world’s'
        ' most populous metropolitan area.'
    },
    'Paris': {
        'country': 'France',
        'population': 2140526,
        'area': 105.4,  # in square kilometers
        'currency': 'Euro',
        'famous_landmarks': ['Eiffel Tower', 'Louvre Museum', 
                             'Notre-Dame Cathedral'],
        'fact': 'Paris is famous for its art, fashion,'
        ' and the iconic Eiffel Tower.'
    },
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'area': 789,  # in square kilometers
        'currency': 'Dollar',
        'famous_landmarks': ['Statue of Liberty', 'Times Square', 
                             'Central Park'],
        'fact': 'New York City is known as "The Big Apple" and is home to'
        ' Times Square and Central Park.'
    }
}

# Loop through the dictionary and print each city's information:
for city, info in cities.items():
    print(f"City: {city}")
    print(f" - Country: {info['country']}")
    print(f" - Population: {info['population']:,}") 
    print(f" - Area: {info['area']} km²")
    print(f" - Currency: {info['currency']}")
    print(f" - Famous Landmarks: {', '.join(info['famous_landmarks'])}")
    print(f" - Fact: {info['fact']}")
    print('-' * 40)