


"""Generation password"""

import random
import time


def password_gen(leight):
    digits = '0123456789'
    litters_1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    litters_2 = 'abcdefghijklmnopqrstuvwxyz_'
    my_password = digits + litters_1 + litters_2
    password = []

    password.append(random.choice(digits))
    password.append(random.choice(litters_1))
    password.append(random.choice(litters_2))
    result_list = password + random.sample(my_password, 5)
    random.shuffle(result_list)

    for i in range(len(result_list) - 1):
        while result_list[i] == result_list[i + 1]:
            random.shuffle(result_list)
    return ''.join(result_list)


final_password = password_gen(8)


def main():
    print('Password is being generated...')
    time.sleep(3)

    print(final_password)


if __name__ == '__main__':
    main()
