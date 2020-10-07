# Import Math Module.

import math

# Greet the user and request information.

print('Welcome to the velocity calculator. Please enter the following: ')

# Line break.

print()

# Prompt user for information.

m = float(input('Mass (in kg): '))
g = float(input('Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): '))
t = int(input('Time (in seconds): '))
p = float(input('Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): '))
A = float(input('Cross sectional area (in m^2): '))
C = float(input('Drag constant (0.5 for sphere, 1.1 for cylinder): '))

# Line break.

print()

# Calculate the inner value of c.

c = (1 / 2) * p * A * C

# Calculate the overall velocity of the dropped object.

velocity = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c)/ m) * t))

print(f'The inner value of c is: {round(c, 3)}')
print(f'The velocity after {round(t, 1)} seconds is: {round(velocity, 3)} m/s')