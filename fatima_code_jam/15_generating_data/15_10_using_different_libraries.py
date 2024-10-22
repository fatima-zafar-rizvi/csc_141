
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


import plotly.graph_objects as go
import random

class RandomWalk:
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = random.choice([1, -1])
        distance = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        return direction * distance

# Create a random walk and visualize it with Plotly
rw = RandomWalk(5000)
rw.fill_walk()

fig = go.Figure()
fig.add_trace(go.Scatter(x=rw.x_values, y=rw.y_values, mode='lines', line=dict(width=2, color='blue')))
fig.update_layout(title='Random Walk Visualization', xaxis_title='X Coordinate', yaxis_title='Y Coordinate')
fig.show()