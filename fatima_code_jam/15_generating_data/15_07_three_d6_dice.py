
import numpy as np
import matplotlib.pyplot as plt

# Simulate rolling three D6 dice
num_rolls = 1000
die1 = np.random.randint(1, 7, size=num_rolls)
die2 = np.random.randint(1, 7, size=num_rolls)
die3 = np.random.randint(1, 7, size=num_rolls)
results = die1 + die2 + die3  # Sum of the three dice

# Plotting the results
plt.figure(figsize=(10, 6))
plt.hist(results, bins=np.arange(3, 20) - 0.5, edgecolor='black', alpha=0.7)
plt.title('Results of Rolling Three D6 Dice 1,000 Times')
plt.xlabel('Sum of Dice')
plt.ylabel('Frequency')
plt.xticks(range(3, 19))
plt.grid()
plt.show()