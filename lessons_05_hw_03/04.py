"""Сalculation
leap year"""
print('Do you want to know if the year is a leap year?')
year = int(input('Enter year: '))

if year % 100 == 0 and year % 400 != 0:
    print('No')
elif year % 4 == 0:
    print('Yes')
else:
    print('No')
