# Create line break between the terminal and the program.
print()

# Create empty lists for loop.
names = []
balances = []

# Set default value for loop.
name = None

# Ask user for account names and balances until user terminates
# program.
while name != 'Quit':
    name = input('What is the name of the account? ').capitalize()
    if name != 'Quit':
        balance = float(input('What is the balance of the account? '))

# Add user input account names and balances into the appropriate list.    
        names.append(name)
        balances.append(balance)


# Set default value for loop.
total = 0

print()
print('Account Information:')

# Iterate through names list and display each account name along
# with its coresponding account balance.
for i in range(len(names)):
    print(f'{names[i]} - {balances[i]}')

# Add the totals of the balances together and store in total.
    total += balances[i]

# Compute the average balance of all accounts.
average = total / len(balances)

# Display the total and average to user.
print()
print(f'Total: ${total:.2f}')
print(f'Average: ${average:.2f}')
