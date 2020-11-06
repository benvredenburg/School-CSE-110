# Receive favorite number from user.

fav_num = int(input('What is your favorite whole number? '))

count = 0

for num in range(fav_num + 1):
    count = count + num


# Display the sum of all numbers between 0 and the user input.

print(f'The sum of the numbers from 0 through {fav_num} is: {count}')