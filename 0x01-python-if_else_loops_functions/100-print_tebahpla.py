#!/usr/bin/python3
for aa in range(122, 96, -1):
    print('{:c}'.format(aa if aa % 2 == 0 else aa - 32), end='')
