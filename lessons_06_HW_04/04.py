"""Twelve digit number"""
from random import randint



def get_max_digit(number):
    print('Number =',number)
    maximal = 0

    while number > 0:
         last = number % 10
         if last > maximal:
             maximal = last
         number = number // 10

    print('Maximal number: ', maximal)
    return maximal

number = randint(100000000000,999999999999)
get_max_digit(number)


def get_max_digit(number):
    my_str = str(number)

    for _ in my_str:
        maximal_number = max(my_str)
    print('Maximal number',maximal_number)

    return maximal_number


get_max_digit(number)
