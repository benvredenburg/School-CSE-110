# Create list of colors.

colors = ['red', 'blue', 'green', 'yellow']

# Display each color in list one at a time.

for color in colors:
    print(color)

# Display 1-8.

for i in range(1, 9):
    print(i)

answer = ''

while answer != 'yes':
    answer = input('May I have a piece of candy? ').lower()

print('Thank you.')