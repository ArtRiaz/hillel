# Вычеслить площадь и периметр прямоугольного треугольника

import math

print('Введите значение двух катетов треугольника')
a = float(input('Введите длинну треугольника: '))
b = float(input('Введите высоту треугольника: '))


def triangle_area_and_perimeter(a, b):
    c = math.sqrt(a ** 2 + b ** 2)  # Находим гипотинузу
    return a * b / 2, a + b + c


print(triangle_area_and_perimeter(a, b))