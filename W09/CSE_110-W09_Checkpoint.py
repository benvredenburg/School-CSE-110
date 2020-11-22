# Create a line break between the terminal and the program.
print()

# Create open list.
friends = []

# Create open variable for loop default.
new_friend = ''

# Receive names from user until they end program.
print('Please enter the word "end" when you have completed your list')
print()
while new_friend != 'End':
    new_friend = input('Type the name of a friend: ').capitalize()
    
    if new_friend != 'End':
        friends.append(new_friend)

# Create a line break between the inputs and the printed list.
print()
print('Your friends are:')

for friend in friends:
    print(friend)
    
# Create a line break between the list and the terminal re-prompt
print()