#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
mod = abs(number) % 10
if mod < 6 and mod != 0:
    print (f"Last digit of {number} is {mod} and is less than 6 and not 0")
elif mod == 0:
    print (f"Last digit of {number} is {mod} and is 0")
else:
    print (f"Last digit of {number} is {mod} and is greater than 5")
