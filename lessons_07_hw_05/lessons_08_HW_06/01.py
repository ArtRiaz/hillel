"""Deepcopy without
 deepcopy for tuple and dict"""


def copydeep(value):
    if isinstance(value, tuple):
        return tuple(map(copydeep, value))
    if isinstance(value, dict):
        return {copydeep(key): copydeep(value)
                for key, value in value.items()
                }
    return value


orig_list = [42, 73, (12, 4, 'a')]
copy_list = copydeep(orig_list)
print(copy_list, orig_list)
