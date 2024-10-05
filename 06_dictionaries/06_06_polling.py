# Using favorite_languages.py code from page 96:

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

polling = ['jen', 'sarah', 'ben', 'john', 'oliver', 'phil', 'edward']

for person in polling:
    if person in favorite_languages:
        print(f"\n Thank you, {person.title()}, for responding!")
    else:
        print(f"\n {person.title()}, please take our poll.")