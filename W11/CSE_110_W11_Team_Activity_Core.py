# Open the file.

with open('W11hr_system.txt') as hr_file:
    for line in hr_file:
        line = line.split()
        name = line[0]
        job_title = line[2]

        print(f'Name: {name}, Title: {job_title}')        