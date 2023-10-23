#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    aa = 0
    new_list = []
    for aa in range(0, list_length):
        try:
            result = my_list_1[aa] / my_list_2[aa]
        except ZeroDivisionError:
            result = 0
            print('division by 0')
        except TypeError:
            result = 0
            print('wrong type')
        except IndexError:
            result = 0
            print('out of range')
        finally:
            pass
        new_list.append(result)
    return new_list
