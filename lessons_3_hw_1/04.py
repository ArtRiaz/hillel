 Имя Фамилия кол-во лет
print('Привет , чтобы узнать возраст человека введите по такому примеру Taras Shevchenko*1814-03-09*1861-03-10')
a =  input('Ввод: фамилия имя * дата рождения ГГГГ-ММ-ЧЧ * сегодняшняя дата ГГГГ-ММ-ЧЧ ')
c = a.replace('*',' ')
b = c.split()

name = b[0]+ ' '+b[1]
data1 = (b[3])

age1 = int(data1[:4])
data2 = (b[2])
age2 = int(data2[:4])
age = age1 - age2

print('Name: ', name)
print('Age: ', age)
