#!/usr/bin/python3
for aa in range(0, 10):
    for bb in range(aa + 1, 10):
        print('{:d}{:d}'.format(aa, bb), '\n' if (aa == 8 and bb == 9) else ', ',
              sep='', end='')
