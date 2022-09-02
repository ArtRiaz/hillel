# snake_case это формат написания слов без пробелов разделяющее нижнее подчеркивание funny__one__day
# CamelCase - это формат написание слов с заглавной буквы и вместе FunnyOneDay
print('Преобразование snake_case в Camel Case')
a = input('Введите слова в формате snake_case: ')
b = a.replace('_',' ')
c = b.title()
d = c.replace(' ','')
print('Слова в формате Camel Case:', d)



print('Преобразование snake_case в Camel Case')
a = input('Введите слова в формате snake_case: ')

b = a.title()
c = b.split(sep= '_')
d = ''.join(c)
print('Слова в формате Camel Case:', d)

