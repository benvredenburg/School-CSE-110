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

    # Iterate through the life expectancy column to find and display
    # the lowest number.

    lowest = 100
    for row in life_file:
        clean_row = row.strip()
        clean_row = clean_row.split(',')
        if float(clean_row[3]) < lowest:
            lowest = float(clean_row[3])

    print(f'The lowest life expectancy was {lowest} years')

# Creat a line break for readability.
print()

# Open csv for use and auto closure.
with open('W11life-expectancy.csv', 'r') as life_file:

    # Create reader for csv file.
    csvreader = csv.reader(life_file)

    # Skip header.
    next(csvreader)

    # Iterate through the life expectancy column to find and display
    # the lowest number.

    highest = 0
    for row in life_file:
        clean_row = row.strip()
        clean_row = clean_row.split(',')
        if float(clean_row[3]) > highest:
            highest = float(clean_row[3])

    print(f'The highest life expectancy was {highest} years')

# Creat a line break for readability.
print()