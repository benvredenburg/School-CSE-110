# Receive information from the user about meal prices and number of meals.

ch_meal = float(input("What is the price of a child's meal? $")) 
ad_meal = float(input("What is the price of an adult's meal? $"))
# Used double quotes to compensate for apostrophe in question
num_ch = int(input('How many children are there? '))
num_ad = int(input('How many adults are there? '))
tax_rate = float(input('What is the sales tax rate? '))

# Calculate the sub total of the meal (pre-tax).

sub = round(num_ch * ch_meal + num_ad * ad_meal, 2)

# Calculate the sales tax.

tax = round(sub * tax_rate / 100, 2)

# Calculate the total sale.

total = round(sub + tax, 2)

# Line break.

print()

# Display subtotal, sales tax, and total to user.

print(f'Subtotal: ${sub:.2f}')
print(f'Sales Tax: ${tax:.2f}')
print(f'Total: ${total:.2f}')

# Line break

print()

# Receive totla payment amount from customer.

payment = float(input('What is the payment amount? $'))

# Did the customer leave a tip?

tip = float(input('Tip? $'))

# Calculate change to be returned to user.

change = round(payment - tip - total, 2)

# Display change to be returned to customer to user.

print(f'Change: ${change:.2f}')
