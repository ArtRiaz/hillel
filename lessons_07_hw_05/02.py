""""Create a function
copydeep,without deepcopy"""


def copydeep(lst):
    return [
        elem if not isinstance(elem, list)
        else copydeep(elem)
        for elem in lst
    ]


list1 = [42, 73, ['abc']]
copy_list = copydeep(list1)
list1[2].append(73)
print(copy_list)
print(list1)
