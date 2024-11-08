# Challenge level 9/10

# Original file_reader.py
'''
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    print(line)
'''

# Modified version of file_reader.py
from pathlib import Path 

path = Path('pi_digits.txt')

for line in path.read_text().splitlines():
    print(line)

# Original pi_string.py
'''
from pathlib import Path 

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

'''

# Modified version of pi_string.py
from pathlib import Path 

path = Path('pi_million_digits.txt')
pi_string = ''
for line in path.read_text().splitlines():
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))

# Original pi_birthday.py
'''
from pathlib import Path 

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
'''

# Modified version of pi_birthday.py
from pathlib import Path 

path = Path('pi_million_digits.txt')
pi_string = ''
for line in path.read_text().splitlines():
    pi_string += line.lstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")