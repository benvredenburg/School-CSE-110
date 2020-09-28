# Prompt user for their age and convert their input
# into an Integer stored in a variable.

age = int(input('How old are you? '))

# Display how old the user will be on their next birthday.

print(f'On your next birthday, you will be {age + 1} years old.')

# Line Break.

print()

# Prompt user for how many egg cartons they have in
# their fridge, convert it into an integer stored in 
# a variable.

eggs = int(input('How many egg cartons do you have? '))

# Display how many eggs the user has in their fridge.

print(f'You have {eggs *12} eggs in your fridge.')

# Line Break.

print()

# Prompt the user for how many cookies they have and 
# how many people are with them, convert their answers
# into integers stored in variables.

cookies = int(input('How many cookies do you have? '))
ppl = int(input('How many people are there? '))

# Calculate how many cookies each person can have.

print(f'Each person may have {cookies / ppl} cookies.')