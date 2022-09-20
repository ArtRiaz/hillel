"""Calculate
intersect circles"""

print('Enter the coordinates and radius of circle number one')
x1 = float(input('Enter the coordinates x: '))
y1 = float(input('Enter the coordinates y: '))
r1 = float(input('Enter radius: '))

print('Enter the coordinates and radius of circle number two')
x2 = float(input('Enter the coordinates x: '))
y2 = float(input('Enter the coordinates y: '))
r2 = float(input('Enter radius: '))


def circles_intersect(x1, y1, r1, x2, y2, r2):
    distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return (r2 - r1) **2 <= distance <= (r1 + r2) ** 2


if circles_intersect(x1, y1, r1, x2, y2, r2) is True:
    print('Circle 1 and Circle 2 intersect')
else:
    print('Circle 1 and Circle 2 do not overlap')

circles_intersect(x1, y1, r1, x2, y2, r2)
