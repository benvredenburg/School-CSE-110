# Set condition variable.

is_allowed = False

# Ask for age and height of first rider.

first_age = int(input('What is the age of the first rider? '))
first_height = int(input('What is the height of the first rider? '))

# Ask if there is a second rider.

second_rider = input('Is there a second rider (yes/no)? ')

if second_rider.lower() == 'yes':
    second_age = int(input('What is the age of the second rider? '))
    second_height = int(input('What is the height of the second rider in inches? '))

    if first_height < 36 or second_height < 36:
        is_allowed = False
    
    else:
        if first_age >= 18 or second_age >= 18:
            is_allowed = True

        else:
            is_allowed = False

else:

    if first_age >= 18 and first_height >= 62:
        is_allowed = True
    
    else:
        is_allowed = False

if is_allowed:
    print('Welcome to the ride. Please be safe and have fun!')

else:
    print('Sorry, you may not ride')