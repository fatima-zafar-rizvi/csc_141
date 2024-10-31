import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        result = random.randint(1, self.sides)
        print(f'Rolled a {self.sides}-sided die: {result}')
        return result

# Create a 6-sided die and roll it 10 times
six_sided_die = Die(6)
print("Rolling the 6-sided die 10 times:")
for _ in range(10):
    six_sided_die.roll_die()

# Create a 10-sided die and roll it 10 times
ten_sided_die = Die(10)
print("\nRolling the 10-sided die 10 times:")
for _ in range(10):
    ten_sided_die.roll_die()

# Create a 20-sided die and roll it 10 times
twenty_sided_die = Die(20)
print("\nRolling the 20-sided die 10 times:")
for _ in range(10):
    twenty_sided_die.roll_die()