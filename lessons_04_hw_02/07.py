print('Чтобы узнать сумму трехзначного числа')
a = input('Введите трезначное число: ')


def chislo(a):
    print(ord(a[0]) - 48 + ord(a[2]) - 48 + ord(a[1]) - 48)


chislo(a)
