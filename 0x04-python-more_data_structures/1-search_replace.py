#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if my_list[aa] == search else my_list[aa]
            for aa in range(len(my_list))]
