# Open the file.

with open('W11hr_system.txt') as hr_file:
    for line in hr_file:
        line = line.strip()
        line = line.split()
        name = line[0]
        id_num = line[1]
        job_title = line[2]
        salary = float(line[3])
        paycheck = salary / 24
        eng_bonus = 1000

        if job_title == 'Engineer':
            print(f'{name} (ID: {id_num}), {job_title} - ${paycheck + eng_bonus:.2f}')
        else:
            print(f'{name} (ID: {id_num}), {job_title} - ${paycheck:.2f}')        