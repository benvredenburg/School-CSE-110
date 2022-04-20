import math

# Create line break between terminal and program.
print()

def compute_area_square(side):
    area = compute_area_rectangle(side, side)
    return area

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return math.pi * radius * radius

def compute_area(shape, value1, value2=0):
    area = -1

    if shape == 'Square':
        area = compute_area_square(value1)
    elif shape == 'Circle':
        area = compute_area_circle(value1)
    elif shape == 'Rectangle':
        area = compute_area_rectangle(value1, value2)

    return area

# Create default variable for loop
shape = ''

# Start loop.
while shape != 'Quit':
    shape = input('What kind of shape do you have? ').capitalize()
    print()
    if shape == 'Square':
        side = float(input('What is the length of the side? '))
        area = compute_area(shape, side)
        print(f'The area of the square is {area:.2f} square feet.')
        print()
    elif shape == 'Rectangle':
        length = float(input('What is the length of the rectangle? '))
        width = float(input('What is the width of the rectangle? '))
        area = compute_area(shape, length, width)
        print(f'The area of the rectangle is {area:.2f} square feet.')
        print()
    elif shape == 'Circle':
        radius = float(input('What is the radius of the circle? '))
        area = compute_area(shape, radius)
        print(f'The area of the circle is {area:.2f} square feet.')
        print()
    else:
        print('Please enter a valid shape.')
        print()
print('Goodbye')
print()