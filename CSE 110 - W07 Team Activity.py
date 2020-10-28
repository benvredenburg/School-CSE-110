# Ask user for number.

user_choice = int(input('What number would you like? '))

# Create multiplication table.

for row_number in range(1, user_choice + 1):
    for col_number in range(1, user_choice + 1):
        number = row_number * col_number
        print(f'{number:4}', end=' ')
    print()