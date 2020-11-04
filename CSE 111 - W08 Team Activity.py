# Import random module.

import random

# Line break from terminal for readability.

print()

# Generate a random number and store it in a variable.

answer = ''

while answer != 'No':
    magic_number = random.randint(1, 2)

    guess = 0
    guesses = 0

    while guess != magic_number:
        guess = int(input('What is your guess [1 - 100]? '))
        guesses = guesses + 1
        print()
        if guess > magic_number:
            print('Lower')
            print()
        elif guess < magic_number:
            print('Higher')
            print()
        else:
            print('You guess it!')
            print()

    if guesses == 1:
        print(f'Wow, You got it in {guesses} attempt!')
        print()  
    else:     
        print(f'it took you {guesses} guesses.')
        print()
    
    answer = input('Would you like to play again? ').capitalize()
    while answer != 'No' and answer != 'Yes':
        answer = input('Would you like to play again? ').capitalize()
    print()
