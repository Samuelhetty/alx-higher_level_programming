#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_elements = 0
    for aa in range(0, x):
        try:
            print("{}".format(my_list[aa]), end='')
            num_element += 1
        except IndexError:
            break
    print()
    return num_element
