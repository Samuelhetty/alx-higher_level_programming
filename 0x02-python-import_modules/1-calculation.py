#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    syb = ['+', '-', '*', '/']
    log = {0: add, 1: sub, 2: mul, 3: div}
    for aa in log:
        print('{:d} {:} {:d} = {:d}'.format(a, syb[aa], b, log[aa](a, b)))

if __name__ == "__main__":
    main()
