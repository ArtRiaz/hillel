"""Checking if
a number is even"""

number = int(input('Enter the number: '))


def is_even(number):
    return number % 2 == 0


if is_even(number) is True:
    print('even number')
else:
    print('ood number')
is_even(number)
