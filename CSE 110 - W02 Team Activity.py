# Greet user and prep them for questionnaire.

print('Hello, please enter the following information:')

print()

# Prompt user for personal information (core).

first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number ((xxx) xxx-xxxx): ')
title = input('Job title: ')
id_num = input('ID number: ')

# Prompt for additional information (stretch).

hair_color = input('Hair color: ')
eye_color = input('Eye color: ')
start_month = input('Starting Month: ')
adv_train   = input('Completed advanced training?: ')

# Display ID card for user (core).
print(f'\nThe ID Card is:')
print('----------------------------------------')
print(f'{last_name.upper()}, {first_name.capitalize()}')
print(title.title())
print(f'ID: {id_num}')
print()
print(email.lower())
print(phone)

# Add additional information (stretch).
print(f'Hair: {hair_color:15} Eyes: {eye_color}')
print(f'Month: {start_month:14} Training: {adv_train}')
print('----------------------------------------')