# Challenge level 9/10

# Define the path to your downloaded text files
file_paths = ["book_01_wind_of_destiny.txt", "book_02_millys_errand.txt"]  

def count_word_occurrences(file_path, word):
    """Counts the occurrences of a word in a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()  
    return text.count(word)

# Iterate over each file and print the count results
for file_path in file_paths:
    count_the = count_word_occurrences(file_path, 'the')
    count_the_space = count_word_occurrences(file_path, 'the ')
    difference = count_the - count_the_space  # Calculate difference
    
    print(f"In file '{file_path}':")
    print(f" - Count of 'the' (all occurrences): {count_the}")
    print(f" - Count of 'the ' (specific to 'the' with a space after): "
          f"{count_the_space}")
    print(f" - Difference (extra matches without space): {difference}\n")