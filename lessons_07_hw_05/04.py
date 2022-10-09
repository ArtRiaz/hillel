"""Generation password"""
import random
import time


def password_gen(length):
    digits = '0123456789'
    litters_1 = 'ABCDEFGHIJKLMNOPQRTUVWXYZ'
    litters_2 = 'abcdefghijklmnopqrstuvwxyz_'
    my_password = digits + litters_1 + litters_2
    password = []

    while len(password) < length:
        a = random.choice(my_password)
        password.append(a)
    if not any(char in password for char in digits):
        return password_gen(length)
    elif not any(char in password for char in litters_1):
        return password_gen(length)
    elif not any(char in password for char in litters_2):
        return password_gen(length)

    return ''.join(password)


password_gen(8)


def main():
    print('Password is being generated...')
    time.sleep(3)
    print(password_gen(8))


if __name__ == '__main__':
    main()
