import math

# Create line break between terminal and program.
print()

def compute_area_square(side):
    return side * side

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

# Create default variable for loop
shape = ''

# Start loop.
while shape != 'Quit':
    shape = input('What kind of shape do you have? ').capitalize()
    print()
    if shape == 'Square':
        side = float(input('What is the length of the side? '))
        area_square = compute_area_square(side)
        print(f'The area of the square is {area_square:.2f} square feet.')
        print()
    elif shape == 'Rectangle':
        length = float(input('What is the length of the rectangle? '))
        width = float(input('What is the width of the rectangle? '))
        area_rect = compute_area_rectangle(length, width)
        print(f'The area of the rectangle is {area_rect:.2f} square feet.')
        print()
    elif shape == 'Circle':
        radius = float(input('What is the radius of the circle? '))
        area_circ = compute_area_circle(radius)
        print(f'The area of the circle is {area_circ:.2f} square feet.')
        print()
    else:
        print('Please enter a valid shape.')
        print()
print('Goodbye')
print()