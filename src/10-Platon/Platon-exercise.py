import sys
sys.path.append('..')
from utilities import pow, karatsuba, profiler
from math import log10 as log, e as epsilon
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


def sum_divisors(n:int):
    sum = 0
    for i in range(1, n+1):
        if n%i==0:
            sum+=i
    return sum


def feature(n:int)->float:
    # e_g = pow(epsilon,gamma)
    ln = log(log(n))
    return egamma*n*ln


def solve():
    s5040 = sum_divisors(5040)
    for i in range(5030, 10**7 ): # pow(10,7)
        s = sum_divisors(i)
        # s = len(divisors(i))
        feat = feature(i)
        # if s> s5040:
        #     print(i)
        if s>feat:
            print(f'{i} -> sum: {s} _ condition: {feat}')
            # print(s)



solve()
