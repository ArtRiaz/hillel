
"""Extract a list of
names from a file"""

def list_surname():
    my_list = []
    with open('names.txt') as file:
        for line in file:
            surname = line.split()
            my_list.append(surname[1])
        return my_list


list_surname()
