# Challenge level 2/10

from pathlib import Path

# Read the contents of the file and print it entirely
path = Path('learning_python.txt') 
content = path.read_text()
print("Contents of the file when read entirely:")
print(content)

# Read the contents line by line and store them in a list
path = Path('learning_python.txt')
lines = path.read_text()
print("Contents of the file when read line by line:")
for line in lines:
    print(line, end='')  # end='' to avoid double new lines