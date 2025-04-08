import matplotlib.pyplot as plt
import numpy as np

edges=[0, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]
runtime=[0.00535893440246582, 0.01828742027282715, 0.09677791595458984, 1.0165784358978271, 0.20036840438842773, 2.3099515438079834, 0.5603864192962646, 0.5531883239746094, 1.2475063800811768, 2.019157648086548, 2.0568320751190186, 2.365900754928589, 2.700695037841797, 4.54989767074585, 3.971385955810547, 4.054476737976074, 3.228315830230713, 3.2367327213287354, 3.2759592533111572, 3.2067320346832275, 3.2134203910827637, 3.288393259048462, 3.260768413543701, 3.387584686279297, 3.2503418922424316]
vertices = 50  # Constant number of vertices

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(edges, runtime, marker='s', linestyle='--', color='b', label='Integer Linear Programming (ILP)')

# Add title and labels
plt.title(f'Runtime vs Number of Edges (ILP) \n(Vertices = {vertices})', fontsize=14)
plt.xlabel('Number of Edges', fontsize=12)
plt.ylabel('Runtime (seconds)', fontsize=12)

# Add gridlines
plt.grid(True, linestyle='--', alpha=0.7)

# Add legend
plt.legend(fontsize=10)

# Show the plot
plt.tight_layout()
plt.savefig("ILP_ET_plt.png")
plt.show()
