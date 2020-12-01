from datetime import datetime

''' First Video '''

# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
#     print()

# first_name = 'Susan'
# print_time('first name assigned')

# for x in range(0, 10):
#     print(x)
# print_time('loop completed')


# def get_initial(name):
#     initial = name[0:1].upper()
#     return initial


# first_name = input('Enter your first name: ')
# last_name = input('Enter your last name: ')


# print('Your initials are: ' + get_initial(first_name) + get_initial(last_name))

''' Second Video '''

def get_initial(name, force_uppercase=True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input('Enter your first name: ')
first_name_initial = get_initial(first_name)


print('Your initial is: ' + first_name_initial)