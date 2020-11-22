# Create line break between the terminal and the program.
print()

print("Enter the names and balances of bank accounts (type: quit when done)")

# Create a line break for readability.
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

# Set default values for loops.
highest_name = None
highest_balance = -1

# Iterate through names list and determine the account with the 
# highest balance.
for i in range(len(names)):
    name = names[i]
    balance = balances[i]

    if balance > highest_balance:
        highest_balance = balance
        highest_name = name

# Display account with highest balance.
print(f'The account with the highest balance is: {highest_name} - ${highest_balance:.2f}')

# Create a line break for readability.
print()

# Set default value for loop.
change_account = 'Yes'

# Ask user if they would like to make a change to an account.
while change_account == 'Yes':
    change_account = input('would you like to update an account? ').capitalize()

    # Create a line break for readability.
    print()

# Receive input from user to change account with.
    if change_account == 'Yes':
        index = int(input('Which account index would you like to update? '))

        # Create a line break for readability.
        print()

        new_amount = float(input('What is the new amount? '))

        # Create a line break for readability.
        print()

        balances[index] = new_amount

# Display balances to user.
    print('Account Information: ')
    
    # Create a line break for readability.
    print()
    
    for i in range(len(names)):
        print(f'{i}. {names[i]} - ${balances[i]:.2f}')

        # Create a line break for readability.
        print()