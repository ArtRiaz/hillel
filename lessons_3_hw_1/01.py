#Поменять местами  a и b
a = 'Victoria'
b = 'Regina'

c = a
a = b
b = c

print('Имя а =', a)
print('Имя b =', b)



a = list(range(1,11))
b = list(range(5,16))
a,b = b,a

print('Значения списка а =', a)
print('Значения списка b =', b)



a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
a = a + b
b = a - b
a = a - b
print('Значение а = ', a)
print('Значение b = ', b)
