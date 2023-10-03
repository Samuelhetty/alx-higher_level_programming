#!/usr/bin/python3
for aa in range(0, 100):
    print('{:02d}'.format(aa), ', ' if aa < 99 else '\n', sep='', end='')
