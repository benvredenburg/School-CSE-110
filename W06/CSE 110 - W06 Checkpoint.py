# Create space.

print()

# Set parameter for input for user.
# 1 -10 scale presumably is based from an external rating system against real world dollar values (ex: a 5 for loan size may mean $70,000 
# and a 4 for income may mean an income of $65,000/yr). Response values would need to be adjusted in real world scenarios to account for 
# company scale.

print('Please answer the following questions on a scale of 1 - 10:')

# Line break.

print()

# Ask user questions and store their answers as variables.

loan_size = int(input('How large is the requested loan? '))
credit = int(input('How good is the client credit history? '))
income = int(input('How high is the client income? '))
down_payment = int(input('How large is the client down payment? '))

# Set default value to false.

should_loan = False

# Calculate loan approval from user inputs.

if loan_size >= 5:
    if credit >= 7 and income >= 7:
        should_loan = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else: 
        should_loan = False
else:
    if credit < 4:
        should_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False

# Line Break

print()
# Display decision to user.

if should_loan == True:
    print('Loan is safe. Grant the loan')
else:
    print('Loan is not safe. Deny the loan.')

# Line Break

print()