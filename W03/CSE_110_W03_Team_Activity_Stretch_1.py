import math

# Receive a single length value from user.

length = float(input('What is the length of the line? '))

# Compute the area of a square, circle, and volume of a cube and sphere with the user input userd
# as the length of the lines of the square and cube and length of the radius of the circle and sphere.

square = round(length ** 2, 2)
circle = round(math.pi * length ** 2, 2)
cube = round(length ** 3, 2)
sphere = round(4 / 3 * math.pi * length ** 3, 2)

# Display areas and volumes of square, circle, cube, and sphere to user.

print(f'The area of a square: {square}')
print(f'The area of a circle: {circle}')
print(f'The volume of a cube: {cube}')
print(f'The volume of a sphere: {sphere}')