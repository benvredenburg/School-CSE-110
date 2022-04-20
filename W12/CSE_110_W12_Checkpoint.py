# Create a line break between the terminal and program.
print()

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest = 100
youngest_list = []

for i in people:
    i = i.split()
    if int(i[1]) < youngest:
        youngest = int(i[1])
        youngest_list = i
print(f'The youngest person is {youngest_list[0]} with an age of {youngest_list[1]}')