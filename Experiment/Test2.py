"""
print("Hellow World")

name = "Lukas"

age = 20

print(name, age)

"""

import random

correct_value = random.randint(0, 20)
print(correct_value)

guess_int = -1
while correct_value != guess_int:
    user_guess_str = input("Enter a number between 0 and 20: ")
    guess_int = int(user_guess_str)
    if type (correct_value == guess_int):
        print("The is correct ")
        