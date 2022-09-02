#Оператор * увеличивает итерируемый обьект.Также распаковывает итерируемый обьект в аргументах вызова
#Примеры:

a = list(range(1,11))
b = a * 3
print(b)


q = 'Fanny'
s = q * 3
print(s)


name = ['Artem', 'Victoria', 'Regina']
print(*name)
