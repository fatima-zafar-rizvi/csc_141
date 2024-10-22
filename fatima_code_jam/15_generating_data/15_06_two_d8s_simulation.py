
import numpy as np
import matplotlib.pyplot as plt

# Simulate rolling two D8 dice
num_rolls = 1000
die1 = np.random.randint(1, 9, size=num_rolls)  # Rolls for the first D8
die2 = np.random.randint(1, 9, size=num_rolls)  # Rolls for the second D8
results = die1 + die2  # Sum of the two dice

# Plotting the results
plt.figure(figsize=(10, 6))
plt.hist(results, bins=np.arange(2, 18) - 0.5, edgecolor='black', alpha=0.7)
plt.title('Results of Rolling Two D8 Dice 1,000 Times')
plt.xlabel('Sum of Dice')
plt.ylabel('Frequency')
plt.xticks(range(2, 17))
plt.grid()
plt.show()