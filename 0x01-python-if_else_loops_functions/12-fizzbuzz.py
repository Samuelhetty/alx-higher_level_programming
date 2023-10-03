#!/usr/bin/python3
def fizzbuzz():
    st = ["{:d}", "Fizz", "Buzz", "FizzBuzz"]
    for aa in range(1, 101):
        print(st[(aa % 3 == 0) + 2 * (aa % 5 == 0)].format(aa), end=' ')
