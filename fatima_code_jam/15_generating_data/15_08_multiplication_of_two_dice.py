
import numpy as np
import matplotlib.pyplot as plt

# Simulate rolling two D8 dice for multiplication
num_rolls = 1000
die1 = np.random.randint(1, 9, size=num_rolls)
die2 = np.random.randint(1, 9, size=num_rolls)
results = die1 * die2  # Product of the two dice

# Plotting the results
plt.figure(figsize=(10, 6))
plt.hist(results, bins=np.arange(1, 73) - 0.5, edgecolor='black', alpha=0.7)
plt.title('Results of Multiplying Two D8 Dice 1,000 Times')
plt.xlabel('Product of Dice')
plt.ylabel('Frequency')
plt.xticks(range(1, 65, 5))
plt.grid()
plt.show()