"""Generation password"""
import random
import time


def password_gen(length):
    digits = '0123456789'
    litters_1 = 'ABCDEFGHIJKLMNOPQRTUVWXYZ'
    litters_2 = 'abcdefghijklmnopqrstuvwxyz_'
    my_password = digits + litters_1 + litters_2
    password = ''.join(random.sample(my_password, length))

    if length == 8:
        return (password)
    else:
        return 'Password must be 8 symbol'


password_gen(8)


def main():
    print('Password is being generated...')
    time.sleep(3)
    print(password_gen(8))


if __name__ == '__main__':
    main()