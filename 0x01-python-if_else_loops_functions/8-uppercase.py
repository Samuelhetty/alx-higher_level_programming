#!/usr/bin/python3
def uppercase(str):
    for aa in str:
        print('{:s}'.format(chr(ord(aa) - 32) if ord(aa) > 96 and ord(aa) < 123
                            else aa), end='')
    print()
