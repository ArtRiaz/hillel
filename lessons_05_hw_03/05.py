"""Meaning
funcion sing(x)"""
x = int(input('Enter meaning x: '))


def sign(x):
    return x


if sign(x) > 0:
    print('sing(x)= 1')
elif sign(x) < 0:
    print('sing(x)= -1')
else:
    print('sing(x)= 0')
