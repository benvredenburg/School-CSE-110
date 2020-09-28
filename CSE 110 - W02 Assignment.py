# Prep user for questionnaire.

print('Please enter the following: ')

print()

# Prompt user for words to be used in madlib (core).

adj = input('Adjective: ')
ani = input('Animal: ')
verb_1 = input('Verb: ')
exclamation = input('Exclamation: ')
verb_2 = input('Verb: ')
verb_3 = input('Verb: ')

# Pompt user for three more words to be added into the story (stretch).

ani_2 = input('Animal: ')
adv = input('Adverb: ')
verb_4 = input('Verb: ')

# Display story to user with user input words (core).

print(f'\nYour story is:')
print()
print('The other day, I was really in trouble. It all started when I saw a very ')
print(f'{adj} {ani} {verb_1} down the hallway. "{exclamation.capitalize()}!" I yelled. But all ')
print(f'I could think to do was to {verb_2} over and over. Miraculously, ')
print(f'that caused it to stop, but not before it tried to {verb_3} ')
print('right in front of my family.')

# Display addition to story with use input words (stretch).

print()
print('I thought that would be the end of it but as I turned around I saw it, ')
print(f'a giant {ani_2} looming overhead. At first glance, I thought it was fake, ')
print(f'until it decided to {adv} {verb_4} until a tranquilizer dart put it to sleep.')