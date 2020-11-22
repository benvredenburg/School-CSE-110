# Create a line break between the terminal and the program.
print()

# Create an open list.
numbers = []

# Create a default variable for loop.
new_number = -1

# Receive numbers from user until they end program.
print('Enter a list of numbers, type 0 when finished.')
print()
while new_number != 0:
    new_number = int(input('Enter number: '))

    if new_number != 0:
        numbers.append(new_number)
    
num_sum = sum(numbers)
num_len = len(numbers)
num_avg = round(num_sum / num_len, 2)


# Create a line break between the inputs and the printed statements.
print()

# Display the sum of all numbers in the list.
print(f'The sum is: {num_sum}')

# Display the average of all numbers in the list.
print(f'The average is: {num_avg}')

# Create a default variable for loop.
highest = -1

# Iterate through list to find highest largest number.
for number in numbers:
    if number > highest:
        highest = number

print(f'The largest number is: {highest}')

# Create a line break between the program and the terminal reset.
print()