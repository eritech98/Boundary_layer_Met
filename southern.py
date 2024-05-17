import numpy as np
import matplotlib.pyplot as plt

# Define parameters
D = 1000  # Ekman layer depth in meters
z = np.linspace(0, 3*D, 500)  # Height array

# Geostrophic wind components (assuming purely zonal wind, vg = 0)
ug = 1  # We can set ug to 1 for normalization
vg = 0

# Calculate normalized wind components for Southern Hemisphere
u_ug = 1 + np.exp(-z/D) * np.cos(z/D)  # Change sign from - to +
v_ug = -np.exp(-z/D) * np.sin(z/D)     # Change sign from + to -

# Plotting
plt.figure(figsize=(8, 8))
plt.plot(u_ug, v_ug, label='Ekman spiral hodograph')
plt.xlabel(r'$\frac{u}{u_g}$')
plt.ylabel(r'$\frac{v}{u_g}$')
plt.title('Hodograph of the Ekman Spiral (Southern Hemisphere)')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()
