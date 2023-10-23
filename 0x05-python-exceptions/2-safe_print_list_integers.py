#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num_int_ptd = 0
    for aa in range(0, x):
        try:
            if isinstance(my_list[aa], int):
                print("{:d}".format(my_list[aa]), end='')
                num_int_ptd += 1
        except (TypeError, ValueError):
            pass
    print()
    return num_int_ptd
