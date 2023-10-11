#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return set([aa for aa in set_1 if aa not in set_2] +
               [bb for bb in set_2 if bb not in set_1])
