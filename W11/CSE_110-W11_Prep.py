    # Opening and reading from files.

# with open('W11courses.txt') as courses_file:
#     for line in courses_file:
#         print(line)

#     print('Goodbye')

# print('The file is now closed')

    # Splitting strings.

# colors = 'red,green,blue,yellow'

# color_parts = colors.split(',')
# # color_parts = ['red', 'green', 'blue', 'yellow']

# print(colors)
# print(color_parts)

    # Removing whitespace from strings.

# name = '\tBenjamin Vredenburg          \n'

# clean_name = name.strip()

# print(f'---{name}---')
# print(f'---{clean_name}---')

    # Putting it together.

with open('W11courses.txt') as courses_file:
    for line in courses_file:
        # line = line.strip()
        parts = line.split(',')

        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3


        print(f'{name} - Grade: {grade:.2f}%, after bonus: {bonus_grade:.2f}%')