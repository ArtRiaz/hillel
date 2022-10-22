
"""Extract a list of
names from a file"""

def surname():

    with open('names.txt') as file:
        my_list = []
        a = list(file)
        a.pop(0)
        a.pop(-1)

        for line in a:
            b = line.split()
            my_list.append(b[1])
        return my_list


a = surname()
print(a)