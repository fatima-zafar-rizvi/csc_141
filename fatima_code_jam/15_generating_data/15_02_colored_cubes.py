
import numpy as np
import matplotlib.pyplot as plt

# First 5000 cubic numbers
n_large = np.arange(1, 5001)
cubes_large = n_large ** 3

plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
plt.scatter(n_large, cubes_large, c=n_large, cmap='viridis', s=1)  # Use a colormap
plt.title('First 5,000 Cubic Numbers')
plt.xlabel('Number (n)')
plt.ylabel('Cubic Number (n^3)')
plt.grid()
plt.colorbar(label='Number (n)')  # Add a color bar
plt.show()