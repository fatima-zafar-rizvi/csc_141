# Challenge level 2/10

from pathlib import Path

# Define the language to replace "Python" with
old_language = "Python"
new_language = "C"

# Read the contents of the file and replace the word
path = Path('learning_python.txt')
lines = path.read_text().splitlines()

# Print each modified line
print("Modified lines:")
for line in lines:
    modified_line = line.replace(old_language, new_language)
    print(modified_line) 