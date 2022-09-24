"""Difference beetween
 odd number and even number"""

from random import randint


def diff_odd_even(num_limit, lower_bound, upper_bound):

    my_list = []
    summa_even = 0
    summa_odd = 0

    for _ in range(num_limit):
        my_list.append(randint(lower_bound, upper_bound))

    for i in my_list:
        if i % 2 == 0:
            summa_even += i
        else:
            summa_odd += i

    differance = summa_even - summa_odd
    return differance

num_limit = int(input('Enter number limit: '))
lower_bound = int(input('Enter lower bound number: '))
upper_bound = int(input('Enter upper bound number: '))

print(diff_odd_even(num_limit, lower_bound, upper_bound))
