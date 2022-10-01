""""Copy list
using the function"""
def my_str(lst):
   lst = str(lst)
   return lst[0]


lst = [472, 326, 1, '1101000', 9, '20', 863, '0']
print(sorted(lst, key=my_str))


def my_float(lst):
   return float(lst)


lst = [5, '9', 0, '452', 6.5, '6', 1, 2]
print(sorted(lst, key=my_float))