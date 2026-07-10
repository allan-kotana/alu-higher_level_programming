#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    total = 0
    for element in my_list:
        if element not in unique:
            unique.append(element)
            total += element
    return total
