import sys
sys.path.append('.')
from utilities import pow_modulus as pow, profiler
from math import log10

def randint(n):
    import random
    return random.randint(2,n)



def find_s_t(n):
    '''
        Find s,t such that 'n-1 = 2^s*t'
        :return: s,t
    '''
    from math import log2
    if n%2!=0:
        return None
    t = n
    while t%2==0:
        t = t//2
    s = log2(n//t)
    return int(s), t


def test_congruence(a,b,n):
    '''
    Test if a is congruence with class b mod n.
    :param a: integer
    :param b: remainder
    :param n: modulo
    :return: Boolean
    '''
    # b = b%n
    return (a%n) == (b%n)




def miller_rabin(n:int, k:int)->int:
    j = 0
    s,t = find_s_t(n-1)
    randints = [randint(n-1) for i in range(k)]
    # print('START')
    # print(f's: {s}\nt-size: {int(log10(t))+1} digits\n')
    for i in range(0,k):
        a = randints[i]
        b = pow(a,t,n)
        # b = (a**t)%n
        if test_congruence(b,1,n):
            j+=1
            if j==k:
                return True
        for r in range(0,s):
            if test_congruence(b,-1,n):
                j+=1
                if j==k:
                    return True
            b = (b**2)%n
        # print('*',end=' ')
    # print(f'\nPrime indications: {j}')
    return False


def unit_test_miller_rabin_prime():
    repeats = 50
    prime  = 10485411
    test = lambda: miller_rabin(prime, repeats)
    isPrime = profiler(test)
    if isPrime:
        print('--> SUCCEED is Prime <--')


def unit_test_miller_rabin_non_prime():
    repeats = 50
    prime  = 10485413
    test = lambda: miller_rabin(prime, repeats)
    isPrime = profiler(test)
    if not isPrime:
        print('--> SUCCEED is NoN-Prime <--')




def testing():
    unit_test_miller_rabin_prime()
    unit_test_miller_rabin_non_prime()


