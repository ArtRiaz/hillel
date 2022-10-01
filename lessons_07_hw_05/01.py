"""Index elements
in list"""


def indx(lst, elem):
    if elem is None:
        return None
    my_list = lst[elem]
    return my_list


indx([1, 2.0, ['b'], 'the final list'], 2)