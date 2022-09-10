# Найти площадь и периметр прямоугольного треугольника

import math
from math import pi

h = float(input('Введите высоту конуса: '))
r = float(input('Введите радиус конуса: '))

def cone_surface_area_and_volume(h,r):
    volume = h/3*pi*r**2 # Формула объёма
    base_area = pi * r**2 # Находим площадь основания конуса
    lateral_area = pi * r * math.sqrt(r**2 + h**2) # Находим площадь боковой поверхности конуса
    return volume, base_area + lateral_area

print(cone_surface_area_and_volume(h,r))