#!usr/bin/python3
def no_c(my_string):
    if my_string:
        my_string = [leta for leta in my_string if leta.lower() != 'c']
        my_string = ''.join(my_string)
    return (my_string)
