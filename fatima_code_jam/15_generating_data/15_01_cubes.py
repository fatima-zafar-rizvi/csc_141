
import numpy as np
import matplotlib.pyplot as plt

# First five cubic numbers
n = np.arange(1, 6)  # Numbers 1 to 5
cubes = n ** 3

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
plt.plot(n, cubes, marker='o', color='blue')
plt.title('First Five Cubic Numbers')
plt.xlabel('Number (n)')
plt.ylabel('Cubic Number (n^3)')
plt.grid()
plt.xticks(n)
plt.yticks(cubes)
plt.show()
