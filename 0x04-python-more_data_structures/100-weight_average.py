#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

        digit1 = 0
        digit2 = 0

        for tup in my_list:
            digit1 += tup[0] * tup[1]
            digit2 += tup[1]

        return (digit1 / digit2)
