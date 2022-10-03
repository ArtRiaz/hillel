"""Index elements
in list"""


def indx(lst, elem):
    for index, value in enumerate(lst, 0):
        if elem == value:
            return index
        elif value is None:
            return None


indx([1, 2.0, ['b'], 'the final list'], 1)
