import sys
sys.path.append('..')
from utilities import pow, karatsuba, profiler
from miller_rabin import miller_rabin
from math import log, e as epsilon, ceil as upper_bound
gamma = 0.577
egamma = epsilon ** gamma

def divisors(n:int):
    divs = []
    for i in range(1, n+1):
        if n%i==0:
            divs.append(i)
    return divs


def sum_divisors_slow(n:int):
    sum = 0
    divs = divisors(n)
    for d in divs:
        sum += d
    return sum


def sum_divisors_old(n: int):
    sum = 0
    max_divisor = (n + 1) // 2
    for i in range(n+1, 1,-1):
        if n % i == 0:
            sum += i
    return sum

def sum_divisors(n: int, limit:int):
    sum = 0
    max_divisor = (n + 1) // 2
    for i in range(max_divisor+1, n//2,-1):
        if n % i == 0:
            sum += i
    if sum>= limit//2:
        for i in range(n//2, 1,-1):
            if n % i == 0:
                sum += i
    return sum


def feature(n:int)->float:
    # e_g = pow(epsilon,gamma)
    ln = log(log(n)) # by default base-e
    return egamma*n*ln


def solve():
    s5040 = sum_divisors_old(5040)
    for i in range(5030, 10**7 ): # pow(10,7)
        s = sum_divisors_old(i)
        # s = len(divisors(i))
        feat = feature(i)
        # if s> s5040:
        #     print(i)
        if s>feat:
            print(f'{i} -> sum: {s} _ condition: {feat}')
            # print(s)

def test(i:int):
    feat = feature(i)
    # s = sum_divisors(i,upper_bound(feat))
    s = sum_divisors_old(i)
    if s > feat:
        print(f'{i} -> sum: {s} _ condition: {feat}')
        return True
    return False


def solve_parallel():
    import os
    from concurrent.futures import ProcessPoolExecutor

    min = 5030
    max = 10**7
    workers = os.cpu_count()

    print(f"\nRun parallel\nnumber-of-workers: {workers}\ntest-range: [{min},{max}]\n")
    executor = ProcessPoolExecutor(max_workers=workers)
    results = executor.map(test, list(range(min, max )))

    proves = sum(list(results))
    if proves==1:
        print('Platon\'s statement is True.')
    else:
        print(f'Platon has failed !!!\nFind total: {proves}')


solve_parallel()

# import cProfile
# cProfile.run('solve_parallel()')
# cProfile.run('solve()')
