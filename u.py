import numpy as np
import matplotlib.pyplot as plt

# Constants
ug = 1  # assuming u_g is 1 for simplicity

# Range for the angle (theta)
theta = np.linspace(0, 2*np.pi, 1000)

# Calculate u/ug
u_g = 1 - np.exp(-theta) * np.cos(theta)

# Plotting theta against u/ug
plt.figure(figsize=(8, 6))
plt.plot(u_g, theta/np.pi, label='θ')
plt.title('Plot of u/ug against Angle (0 to 2π)')
plt.xlabel('u/ug')
plt.ylabel('Angle (π)')
plt.grid(True)
plt.legend()
plt.show()

