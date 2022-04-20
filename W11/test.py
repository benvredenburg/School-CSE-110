# Import necessary module(s).
import csv

# Creat a line break for readability.
print()

# Open csv for use and auto closure.
with open('W11life-expectancy.csv', 'r') as life_file:

# Create reader for csv file.
    csvreader = csv.reader(life_file)

# Skip header.
    next(csvreader)

# Iterate through the file to determine the lowest and 
# highest life expectancies as well as the average life
# expectancy worldwide for the user's chosen year.
    lowest = 100
    low = []
    highest = 0
    high = []
    average = 0
    average_list = []
    choice1 = int(input('Which year would you like to check the average for? '))
    choice2 = input('Which country would you like to see statistics for? ').capitalize()
    user_lowest = 100
    user_low = []
    user_highest = 0
    user_high = []
    user_average = 0
    user_avg_list = []
    
    for row in life_file:
        row = row.strip()
        row = row.split(',')
        if float(row[3]) < lowest:
            lowest = float(row[3])
            low = row
        if float(row[3]) > highest:
            highest = float(row[3])
            high = row
        if float(row[2]) == choice1:
            average_list.append(float(row[3]))
            average = round(sum(average_list) / len(average_list), 2)
        if row[0] == choice2 and float(row[3]) < user_lowest:
            user_lowest = float(row[3])
            user_low = row
        if row[0] == choice2 and float(row[3]) > user_highest:
            user_highest = float(row[3])
            user_high = row
        if row[0] == choice2:
            user_avg_list.append(float(row[3]))
            user_average = round(sum(user_avg_list) / len(user_avg_list), 2)
            
# Display lowest and highest life expectancies an average 
# life expectancy for user's chosen year.
# Creat a line break for readability.
    print()
    print('The lowest life expectancy ever recorded worldwide was:')
    print(low)
# Creat a line break for readability.
    print()
    print('The highest life expectancy ever recorded worldwide was:')
    print(high)
# Creat a line break for readability.
    print()
    print(f'The average life expectacy recorded worldwide in the year {choice1} was {average} years old')
# Creat a line break for readability.
    print()
    print(f'Statistics for {choice2}')
    
    print()
    print(f'The lowest life expectancy ever recorded in {choice2} was:')
    print(user_low)
# Creat a line break for readability.
    print()
    print(f'The highest life expectancy ever recorded in {choice2} was:')
    print(user_high)
# Creat a line break for readability.
    print()
    print(f'The average life expectacy in {choice2} is {user_average} years old')
# Creat a line break for readability.
    print()