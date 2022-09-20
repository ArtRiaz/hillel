'''Meaning
funcion sing(x)'''
x = int(input('Enter meaning x: '))


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


sign(x)
