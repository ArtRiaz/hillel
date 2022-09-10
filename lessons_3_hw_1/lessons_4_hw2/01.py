# Перевод градусы в радианы

print('Чтобы перевести градусы в радианы')
degrees = float(input('Введите градусы: '))

def degrees2radians(degrees):
   return degrees * 3.14/180
print(degrees2radians(degrees),'Радиан')