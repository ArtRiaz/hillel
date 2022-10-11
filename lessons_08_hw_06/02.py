"""Iterables object"""
def lchain(*iterables):
    result = []
    for i in iterables:
        for elem in i:
            result.append(elem)
    return result


print(lchain([1, 2, 3], {'5': 5}, tuple(), (6, 7), range(8, 10)))
