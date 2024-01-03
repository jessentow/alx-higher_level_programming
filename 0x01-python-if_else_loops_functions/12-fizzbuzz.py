#!/usr/bin/python3

"""Print the numbers from 1 to 100 separated by a space.
  For multiples of 3, print Fizz instead of the number
    For multiples of 3,, print Buzz instead of the number.
      For multiples of 3 and 5, print FizzBuzz instead of the number.
        """


def fizzbuzz():
    for digit in range(1, 101):
        if digit % 3 == 0 and digit % 5 == 0:
            print("FizzBuzz ", end="")
    elif digit % 3 == 0:
        print("Fizz ", end="")
    elif digit % 5 == 0:
        print("Buzz ", end="")
    else:
        print("{} ".format(digit), end="")
