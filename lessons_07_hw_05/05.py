"""List 1 - 100"""

def gen_primes():
    lst = []
    for i in range(1,101):
        if i < 2:
            continue
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


print(gen_primes())
