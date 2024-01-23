#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    turn = 0
    for e in range(x):
        try:
            print("{}".format(my_list[e]), end="")
            turn += 1
        except IndexError:
            break
    print("")
    return (turn)
