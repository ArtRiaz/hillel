"""Solution of
quadratic equations"""

import math

a = float(input('Enter meaning a = '))
b = float(input('Enter meaning b = '))
c = float(input('Enter meaning c = '))


def solve_quadratic_equation(a, b, c, ):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x, None
    else:
        return None, None


print(solve_quadratic_equation(a, b, c, ))
