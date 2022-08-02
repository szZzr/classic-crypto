def pow(base:int, exponent:int, modulus:int=0):
    '''
        A method for exponential calculation.
        :param base:
        :param exponent:
        :return:
        '''
    if modulus==0:
        return pow_regular(base, exponent)
    else:
        return pow_modulus(base,exponent, modulus)


def pow_regular(base:int, exponent:int)->int:
    '''
    Normal exponential calculation.
    :param base:
    :param exponent:
    :return:
    '''
    result = 1
    b = base
    e = exponent
    while e>0:
        if e%2==1:
            result = result*b
            # result = karatsuba(result,b)%m
        e = e//2
        b = (b**2)
    return result



def pow_modulus(base:int, exponent:int, modulus:int)->int:
    '''
    Modulus exponential calculation.
    :param base:
    :param exponent:
    :param modulus:
    :return:
    '''
    result = 1
    b = base
    e = exponent
    m = modulus
    while e>0:
        if e%2==1:
            result = result*b%m
        e = e//2
        b = (b**2)%m
    return result


def pow_modulus2(base:int, exponent:int, modulus:int)->int:
    '''
    Modulus exponential calculation.
    :param base:
    :param exponent:
    :param modulus:
    :return:
    '''
    result = 1
    b = base
    e = exponent
    m = modulus
    while e>0:
        if e%2==1:
            result = result*b%m
            # result = karatsuba(result,b)%m
        e = e//2
        b = (b**2)%m
        print(f'base: {b}\texponent:{e}\tresult:{result}')
    return result


def pow2(base:int, exponent:int, modulus:int):
    from math import log2
    result = 1
    b = base
    e = exponent
    m = modulus
    x = 2**int(log2(e if e>0 else 1))
    e = e//x
    b = (b**x)%m
    while e > 0:
        if e % 2 == 1:
            result = result * b % m
            # result = karatsuba(result,b)%m
        e = e // 2
        b = (b ** 2) % m
        # print(f'base: {b}\texponent:{e}\tresult:{result}')
    return result



def profiler(run_code):
    '''
    Method that estimates the execution time and the calls
    of a given function. The result is printing at the execution
    time.
    :param run_code: Function
    :return: Function's Result.
    '''
    import cProfile, pstats, io
    pr = cProfile.Profile()
    pr.enable()
    result = run_code()
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s)
    ps.print_stats()
    print(s.getvalue())
    return result


def eratosthenes(bound:int)->list:
    '''
    Sieve of Eratosthenes. This method estimates all the
    primes number until the given integer
    :param bound: An integer as enumeration bound.
    :return: List with primes [2,bound]
    '''
    from math import sqrt
    primes = [i for i in range(2,bound+1)]
    index = 0
    prime = 2
    while prime <= int(sqrt(bound+1)):
        prime = primes[index]
        i = index+1
        while i<len(primes):
            if primes[i]%prime==0:
                primes.pop(i)
            else:
                i +=1
        index += 1
    return primes


def karatsuba(x:int,y:int,B:int=10):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    else:
        m = max(len(str(x)),len(str(y)))
        m2 = m // 2
        a= x//B**(m2)
        b= x%B**(m2)
        c= y//B**(m2)
        d= y%B**(m2)
        z0 = karatsuba(b,d,B)
        z1 = karatsuba((a+b),(c+d),B)
        z2 = karatsuba(a,c,B)
        return ( z2 * B**(2*m2) ) + ( (z1 - z2 - z0) * B**(m2) ) + z0


def fibonacci(n:int):
    '''
    Estimates the Fibonacci Sequence.
    Runtime Complexity: O(n)
    Memory Complexity: O(1)
    :param n:
    :return:
    '''
    new = 0 # init
    x = 0 #F_0
    y = 1 #F_1
    if n ==0:
        return x
    if n==1:
        return y
    for i in range(n):
        new = x + y
        x = y
        y = new
    return x


def euclidean(number1, number2):
    x = number1
    y = number2
    while y!=0:
        t = y
        y = x%t
        x = t
    return x


def extended_euclidean(number1, number2):
    '''
    a, b, d = gcd(number1, number2) for a*number1 + b*number2 = d
    For RSA usage
    :param number1: e
    :param number2: phi(N)
    :return:
    '''
    a,b,u,v,x,y = 1,0,0,1,number1,number2
    U,V = 0,0
    while y>0:
        q = x//y
        t = y
        y = x%t
        x = t
        if y==0:
            break
        U = a - q*u
        V = b - q*v
        a = u
        b = v
        u = U
        v = V
    U = U if U>0 else U%number2
    return U,V,x


def lcm(number1, number2):
    x = number1
    y = number2
    gcd = euclidean(number1,number2)
    return x//gcd*y


def save_file(data, path):
    import pickle as pkl
    with open(path, 'wb') as file:
        file.write(pkl.dumps(data))

def load_file(path):
    import pickle as pkl
    with open(path,'rb') as file:
        data = pkl.loads(file.read())
    return data




def eratosthenes2(bound:int)->list:
    '''
    Sieve of Eratosthenes. This method estimates all the
    primes number until the given integer
    :param bound: An integer as enumeration bound.
    :return: List with primes [2,bound]
    '''
    from math import sqrt
    primes = [i for i in range(2,bound+1)]
    index = 0
    prime = 2
    while prime <= int(sqrt(bound+1)):
        prime = primes[index]
        i = index+1
        while i<len(primes):
            if primes[i]%prime==0:
                primes.pop(i)
            else:
                i +=1
        index += 1
    return primes


def run(min,max):
    from time import clock as tstart
    start = tstart()
    l = []
    loops = 0
    try:
        # a = [i for i, _ in enumerate(range(min, max, 2))]
        for i,_ in enumerate(range(min,max)):
            loops = i
            l.append(i)
    except:
        duration = tstart() - start
        print(f'Duration: {duration}\nLoops: {loops}')
        return loops



def decrypt_RSA(cipher:list, d:int, N:int)->list:
    message = [0 for m in cipher]
    for i,c in enumerate(cipher):
        message[i] = pow(c,d,N)
    return message
