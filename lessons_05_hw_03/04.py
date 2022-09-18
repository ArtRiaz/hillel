"""Сalculation
leap year"""
print('Do you want to know if the year is a leap year?')
year = int(input('Enter year: '))

if year % 4 == 0 and year % 400 == 0:
    print('Yes')
elif year % 100 != 0:
    print('No')