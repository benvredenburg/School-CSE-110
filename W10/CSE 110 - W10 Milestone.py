# Create a break line between the terminal and program.
print()

# Create an empty shopping cart list.
cart = []
prices = []
quantities = []

# Create a default variable for the loop.
choice = None

while choice != 5:
    print()
    print('Please select one of the following:')
    print('1. Add item')
    print('2. View cart')
    print('3. Remove Item')
    print('4. Compute total')
    print('5. Quit')
    print()
    
    choice = int(input('Please enter an action: '))
    print()

    if choice == 1:
        item = input('what item would you like to add? ').capitalize()
        price = float(input(f'What is the price of {item}? '))
        quantity = int(input('How many would you like? '))
        cart.append(item)
        prices.append(price)
        quantities.append(quantity)
        print()
        print(f"'{item}' has been added to the cart.")
        print()
    elif choice == 2:
        print()
        print('The contents of your shopping cart are: ')
        print()
        for i in range(len(cart)):
            print(f'[{quantities[i]}] {cart[i]} - ${prices[i]:.2f}')
    elif choice == 3:
        print()
        index = int(input('Which item would you like to remove? '))
        print()
        del cart[index - 1]
        del prices[index - 1] 
        del quantities[index - 1]
    elif choice == 4:
        subtotal = 0
        print()
        for i in range(len(cart)):
            subtotal += prices[i] * quantities[i]
            tax = subtotal * .06
            total = subtotal + tax
        print(f'The total price of the items in the shopping cart is ${total:.2f}')

print('Thank you. Goodbye')