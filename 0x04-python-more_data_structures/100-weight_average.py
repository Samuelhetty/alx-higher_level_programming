#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum, items = 0, 0
        for aa, bb in my_list:
            sum += aa * bb
            items += bb
        return sum / items
    return 0
