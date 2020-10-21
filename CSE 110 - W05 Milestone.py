# Get name for player.

pl_name = input('Greetings! Please enter your name: ').capitalize()

# Line break

print()

# Greet player and ask which adventure they would like to play.

    
choice_1 = input(f'Hello {pl_name}, It is a pleasure to meet you. Would you like to take on the dungeon? ').upper()

# Line Break.

print()

# Begin story.
#status = 0

#while status == 0:

if choice_1 == 'yes'.upper():
    choice_1a = input('You find yourself lying on the floor of a wet, dark, damp cave-like room. To your left, you see a STAFF while to the right, you see a SWORD. Which will you take? ').upper()
        #status = 1

# Line break.

    print()

    #while status == 1:

    if choice_1a == 'staff'.upper():
        choice_2a = input('As your fingers wrap around the staff, you can feel an arcane power take root within you. Do you DROP the staff, STOW it on your back, or TEST it out? ').upper()
            #status = 2

# Line break

        print()

        #while status == 2:

        if choice_2a == 'drop'.upper():
            print('As the staff hits the ground, you awaken in your bed in a cold sweat, unsure if your experience actually happened or was the result of some delerium.')
                #status = 99

        elif choice_2a == 'stow'.upper():
            print('As you strap the staff to your back, a door appears and opens. A mirror image of yourself weilding a sword emerges from the doorway. ') 
                #status = 99

        elif choice_2a == 'test'.upper():
            print('You instinctively know what to do and activate the staff. A bright light shoots out from the tip and reveals to you that you are not alone in this dark, foreboding place. The giant spider recoils for a moment but the moment the light fades, you hear it skittering towards you.')
                #status = 99
    
    elif choice_1a == 'sword'.upper():
        choice_2b = input('You grasp the sword by the hilt and immediately feel the knowledge of how to use it fill your mind. Do you DROP the sword, SHEATHE it on your belt, or give it a few practice SWINGS? ').upper()

        # Line break.

        print()

        if choice_2b == 'drop'.upper():
            print('The sword clanks against the stone, you awaken in your bed in a cold sweat, unsure if your experience actually happened or was the result of some delerium.')

        elif choice_2b == 'sheathe'.upper():
            print('As you sheathe your new weapon, a door appears and opens. A mirror image of yourself weilding a staff emerges from the doorway.')

        elif choice_2b == 'swings'.upper():
            print('As you swing the sword, a dim blue light radiates from the blade and a growling noise comes from deeper within the cave.')

else:
    print('Well, your loss, I guess. Goodbye.')
        #status = 99

# Line break.

print()

if choice_1 == 'yes'.upper():
    print('Please stay tuned for episode 2!')