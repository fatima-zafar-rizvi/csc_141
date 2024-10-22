
import matplotlib.pyplot as plt
from random_walk import RandomWalk  # Assuming you have a RandomWalk class

# Create a RandomWalk instance
rw = RandomWalk(5000)  # Use 5000 points
rw.fill_walk()

# Set up the plot
plt.figure(figsize=(10, 6))
ax = plt.subplot(1, 1, 1)

# Use ax.plot() instead of ax.scatter()
ax.plot(rw.x_values, rw.y_values, linewidth=2)

# Set title and labels
ax.set_title("Molecular Motion of a Pollen Grain")
ax.set_xlabel("X Coordinate")
ax.set_ylabel("Y Coordinate")
plt.show()