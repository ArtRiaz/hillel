"""Сhecking if
a number is even"""

number = int(input('Enter the number: '))


def is_even(number):
   return number

if number % 2 == 0:
   print('even number')
else:
   print('odd number')

is_even(number)

