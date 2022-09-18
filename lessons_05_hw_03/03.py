"""Calculate 
intersect circles"""

import math

print('Enter the coordinates and radius of circle number one')
x1 = float(input('Enter the coordinates x: '))
y1 = float(input('Enter the coordinates y: '))
r1 = float(input('Enter radius: '))

print('Enter the coordinates and radius of circle number two')
x2 = float(input('Enter the coordinates x: '))
y2 = float(input('Enter the coordinates y: '))
r2 = float(input('Enter radius: '))


def circles_intersect(x1, y1, r1, x2, y2, r2):
    diametr = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return diametr


if circles_intersect(x1, y1, r1, x2, y2, r2) < r1 - r2:
    print('Circle 2 is in Circle 1')
elif circles_intersect(x1, y1, r1, x2, y2, r2) < r2 - r1:
    print('Circle 1 is in Circle 2')
elif circles_intersect(x1, y1, r1, x2, y2, r2) > r1 + r2:
    print('Circumference of circle 1 and circle 2 intersect')
else:
    print('Circle 1 and Circle 2 do not overlap')
