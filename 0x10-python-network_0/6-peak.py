#!/usr/bin/python3
# Finds the peak in a list of unsorted integers

def find_peak(list_of_integers):
    """find the peak"""
    if list_of_integers == []:
        return None

    s = len(list_of_integers)
    if s == 1:
        return list_of_integers[0]
    elif s == 2:
        return max(list_of_integers)

    m = int(s / 2)
    p = list_of_integers[m]
    if p > list_of_integers[m - 1] and p > list_of_integers[m + 1]:
        return p
    elif p < list_of_integers[m - 1]:
        return find_peak(list_of_integers[:m])
    else:
        return find_peak(list_of_integers[m + 1:])
