Ask user question.

location = input('Where is the game played? ')

# Compare input to a location.

if location.capitalize() != 'Washington':
    print('This is an away game.')
else:
    print('This is a home game.')

print(location.capitalize() != 'Washington')