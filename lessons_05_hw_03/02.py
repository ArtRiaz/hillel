import math

a = float(input('Enter meaning a = '))
b = float(input('Enter meaning b = '))
c = float(input('Enter meaning c = '))


def solve_quadratic_equation(a, b, c, ):
    discriminant = b ** 2 - 4 * a * c  # Находим дискриминант
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)  # Значение если  discriminant > 0
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)  # Значение если  discriminant > 0
    return x1, x2  # Возвращаем два значения


print(solve_quadratic_equation(a, b, c, ))
