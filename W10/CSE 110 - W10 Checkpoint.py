# Create line break between the terminal and the program.
print()

# Explain use of program to user.
print('Please enter the items of the shopping list (type: quit to finish):')
print()

# Create empty shopping list.
shop_list = []

# Define empty variable for loop.
item = None

# Populate shop_list with user input:
while item != 'Quit':
    item = input('Item: ').capitalize()

    if item != 'Quit':
        shop_list.append(item)
    
print('The shopping list is:')
for item in shop_list:
    print(item)

print('The shopping list with indexes is:')
for i in range(len(shop_list)):
    item = shop_list[i]
    print(f'{i}. {item}')

print()
index = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ').capitalize()

shop_list[index] = new_item

print('The shopping list with indexes is:')
for i in range(len(shop_list)):
    item = shop_list[i]
    print(f'{i}. {item}')