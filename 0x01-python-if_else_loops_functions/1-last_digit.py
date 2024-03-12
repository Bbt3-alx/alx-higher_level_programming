#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_value = abs(number)
l_digit = abs_value % 10
if number < 0:
    neg_last = '-' + str(l_digit)
    l_digit = int(neg_last)

if l_digit > 5:
    print(f"Last digit of {number} is {l_digit} and is greater than 5")

elif l_digit == 0:
    print(f"Last digit of {number} is {l_digit} and is 0")

elif l_digit < 6 and l_digit != 0:
    print(f"Last digit of {number} is {l_digit} and is less than 6 and not 0")
