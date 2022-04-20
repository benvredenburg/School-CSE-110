import math

# Receive a length of a side of a square in cm.

length_sq = float(input('What is the length of a side of the square in cm? '))

# Calculate the area of the square

area_sq = round(length_sq ** 2, 2)

# Display the area of the square in cm and m.

print(f'The area of the square is: {area_sq} cm^2 or {area_sq / 10000} m^2')

# Receive a length and width of a rectangle in cm.

length_rec = float(input('What is the length of the rectangle in cm? '))
width_rec = float(input('What is the width of the rectangle in cm? '))

# Calculate the area of the rectangle

area_rec = round(length_rec * width_rec, 2)

# Display the area of the rectangle in cm and m.

print(f'The area of the rectangle is: {area_rec} cm^2 or {area_rec / 10000} m^2')

# Receive a radius of a circle in cm.

length_cir = float(input('What is the radius of the circle in cm? '))

# Calculate the area of the square

area_cir = round(math.pi * length_cir ** 2, 2)

# Display the area of the circle in cm and m.

print(f'The area of the circle is: {area_cir} cm^2 or {area_cir / 10000} m^2')