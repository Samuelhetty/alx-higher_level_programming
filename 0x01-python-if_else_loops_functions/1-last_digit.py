#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
st = ['Last digit of', 'is', 'and is 0', 'and is greater than 5',
        'and is less than 6 and not 0']
num = number % 10 if number >= 0 else (abs(number) % 10) * -1
print(st[0], number, st[1], num, st[2] if num == 0 else st[3] if num > 5 else st[4])
