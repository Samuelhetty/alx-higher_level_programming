#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    nb_print = 0
    for aa in range(x):
        try:
            print("{}".format(my_list[aa]), end='')
            nb_print += 1
        except IndexError:
            break
    print()
    return nb_print
