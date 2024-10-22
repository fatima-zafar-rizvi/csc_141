
import numpy as np
import matplotlib.pyplot as plt

# Using list comprehension for rolling two D8 dice
num_rolls = 1000
results = [np.random.randint(1, 9) + np.random.randint(1, 9) for _ in range(num_rolls)]

# Visualize using histogram
plt.figure(figsize=(10, 6))
plt.hist(results, bins=np.arange(2, 18) - 0.5, edgecolor='black', alpha=0.7)
plt.title('Results of Rolling Two D8 Dice (Comprehension) 1,000 Times')
plt.xlabel('Sum of Dice')
plt.ylabel('Frequency')
plt.xticks(range(2, 17))
plt.grid()
plt.show()