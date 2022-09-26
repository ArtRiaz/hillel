"""Calculates the sum
 of the symbol code"""

first = input('Enter meaning: ')
last = input('Enter meaning: ')


def sum_symbol_codes(first, last):
    summa = 0

    for i in range(ord(first), ord(last) + 1):
        summa = summa + i
    return summa


sum_symbol_codes(first, last)
