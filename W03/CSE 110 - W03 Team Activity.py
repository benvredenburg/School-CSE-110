import math

# Receive length of a square side from user.

sq = float(input('What is the length of a side of the square? '))

# Calculate the area of the square.

square = round(sq * sq, 2)

# Display the area of the square.

print(f'The area of the square is {square}')

# Receive length and width of a rectangle from user.

length = float(input('What is the length of the rectangle? '))
width = float(input('What is the width of the rectangle? '))

# Calculate the area of the rectangle.

rect = round(length * width, 2)

# Display the area of the square.

print(f'The area of the square is {rect}')

# Receive radius of a circle from user.

rad = float(input('What is the radius of the circle? '))

# Calculate the area of the circle.

circle = round(math.pi * rad ** 2, 2)

# Display the area of the square.

print(f'The area of the circle is {circle}')