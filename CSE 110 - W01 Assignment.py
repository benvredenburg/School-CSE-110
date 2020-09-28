# Receive favorite color input from user.

fav_color = input("What is your favorite color? ")

shirt_color = input("What color shirt are you wearing right now? ")

if {shirt_color.upper()} == {fav_color.upper()}:
    print("Why am I not surprised?")
else:
    print(f"Why aren't you wearing {fav_color}?")
