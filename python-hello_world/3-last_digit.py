#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = str(number)
if number >= 0:
    last_digit = number_string[-1]
else:
    last_digit = "-" + number_string[-1]
if int(last_digit) == 0:
    comp = "and is 0"
elif int(last_digit) > 5:
    comp = "and is greater than 5"
elif int(last_digit) < 6 and int(last_digit) != 0:
    comp = "and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit} {comp}")