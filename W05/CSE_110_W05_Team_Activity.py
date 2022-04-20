# Receive grade percentage from user.

percentage = float(input('What is your grade percentage? %'))

# Line break.

print()

# Determine the letter grade from user input.

if percentage >= 90:
    letter = 'A'

elif percentage >= 80:
    letter = 'B'

elif percentage >= 70:
    letter = 'C'

elif percentage >= 60:
    letter = 'D'

else:
    letter = 'F'

# Stretch 1.

sign = ''

ones = percentage % 10

if ones >= 7:
    sign = '+'

elif ones < 3:
    sign = '-'

else:
    sign = ''

# Stretch 2.

if percentage >= 93:
    sign = ''

# Stretch 3.

if letter == 'F':
    sign = ''


# Line break.

print()

# Display the letter grade to user.

print(f'Your letter grade is {letter}{sign}')

# Line break.

print()

# Determine and display whether the user passed the class.

if percentage >= 70:
    print('Congratulations! You have passed the class.')

else:
    print("Sorry, but you have failed the class. Better luck next time, and don't be afraid to ask questions.") # Used double quotes to account for apostrophe.