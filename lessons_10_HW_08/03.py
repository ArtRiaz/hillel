

def authors():
    dic = []
    with open('authors.txt') as file:
        for line in file:
            value = line.split("-")
            dic.append({'data_original': value[0]})
            pass
        return dic

authors()
