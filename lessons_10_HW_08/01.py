
"""Put the file in the
 list and delete '.' """

def domain():
    with open ('domains.txt') as file:
        my_list = []
        for line in file:
            my_list.append(line.strip('.'))
    return my_list


domain()
