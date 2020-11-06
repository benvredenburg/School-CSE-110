# Receive a Temperature input from user in F.

tempf = int(input('What is the temperature in Fahrenheit? '))

# Calculate the input Temperature in Celsius.

tempc = round((tempf - 32) * 5 / 9, 1)

# Display Temperature in Celcius to user.

print(f'The temperature in Celsius is {tempc} degrees')