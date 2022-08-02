import sys
sys.path.append('..')
from utilities import pow, profiler, eratosthenes

def traditional_to_pow(base:int, exponent:int, modulus:int)->int:
    result = 1
    if exponent==0:
        return result
    for i in range(exponent):
        result = result*base
    result = result - (result//modulus)*modulus
    return result


def keys_finder(g:int, p:int, key:int, primes:bool=False):
    results = []
    if primes:
        candidates = eratosthenes(p-1)
    else:
        candidates = [i for i in range(2,p)]
    for i in candidates:
        for j in candidates:
            if pow(g,i*j,p)==key:
                results.append((i,j))
    return list(dict.fromkeys(results))


def methods_comparison():
    base, exponent, modulus = 2,1234567,157
    print('Starting')


    new_method = lambda: pow(base,exponent,modulus)
    old_method = lambda: traditional_to_pow(base,exponent,modulus)

    result1 = profiler(new_method)
    result2 = profiler(old_method)


    print(f'New Method: {base}^{exponent} mod {modulus} = {result1}')
    print(f'Traditional: {base}^{exponent} mod {modulus} = {result2}')


def exercise_solve():
    test = lambda : keys_finder(13,677,1,False)
    results = profiler(test)
    print(f' Results: {results}\nNumber of Results: {len(results)}')


exercise_solve()
