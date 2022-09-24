"""Output numbers from
1 to 100b changing numbers
 divisible by 3 - Fizz , by 5 Buzz
 and by 3 and 5 - BuzzFizz"""

number = range(1, 101)

for i in number:
    if i % 3 == 0 and i % 5 == 0 :
        i = 'BuzzFizz'
    elif i % 3 == 0:
        i = 'Fizz'
    elif i % 5 == 0:
        i = 'Buzz'
    print(i)