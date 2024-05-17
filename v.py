import numpy as np
import matplotlib.pyplot as plt

# Constants
ug = 1  # assuming u_g is 1 for simplicity.Ug is a constant in this case

# Range for the angle (theta)
theta_ = np.linspace(0*np.pi, 2*np.pi, 1000)

# Calculate v/ug
v_ug = np.exp(-theta_) * np.sin(theta_)

# Plotting theta against v/ug
plt.figure(figsize=(8, 6))
plt.plot(v_ug, theta_/np.pi, label='θ')
plt.title('Plot of v/ug against Angle(0 to 2π)')
plt.xlabel('v/ug')
plt.ylabel('Angle (π)')
plt.grid(True)
plt.legend()
plt.show()

