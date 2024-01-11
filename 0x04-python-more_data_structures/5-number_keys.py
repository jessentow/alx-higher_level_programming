#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    various_keys = list(a_dictionary.keys())

    for i in various_keys:
        num += 1

    return (num)
