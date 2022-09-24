from random import randint


def diff_min_max(num_limit, lower_bound, upper_bound):

    my_list = []
    for _ in range(num_limit):
        my_list.append(randint(lower_bound, upper_bound))
    print(my_list)

    my_list.sort()
    difference = my_list[-1] - my_list[0]
    return difference

num_limit = int(input('Enter number limit: '))
lower_bound = int(input('Enter lower bound number: '))
upper_bound = int(input('Enter upper bound number: '))


print(diff_min_max(num_limit, lower_bound, upper_bound))
