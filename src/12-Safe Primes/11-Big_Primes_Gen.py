import sys
sys.path.append('..')
from utilities import profiler, load_file as load, eratosthenes
from miller_rabin import miller_rabin
from big_primes_utilites import min_max_primes
max_prime_path = "maxPrime2048b.pkl"
min_prime_path = "minPrime2048b.pkl"
Primes16 = eratosthenes(2**16)[1:]
isCongruent = lambda a,b,n: (a%n) == (b%n)


def pPrimes(bits:int):
    primes8 = eratosthenes(2**bits)[1:]
    c_primes = [() for i in primes8]
    for i,r in enumerate(primes8):
        c_primes[i] = ((r-1)//2, r)
    return c_primes

pPrimes8 = pPrimes(bits=8)

def show(isPrime:bool):
    if isPrime:
        result = '*** PRIME ***'
    else:
        result = '-> NoN-PRIME <-'



def p_min_max(bits:int):
    max_prime_path = "maxPrime2048b.pkl"
    min_prime_path = "minPrime2048b.pkl"
    return min_max_primes(max_path=max_prime_path, min_path=min_prime_path, bits=bits)


def q_min_max(p_max, p_min, bits:int=2048):
    max_prime_path = "QmaxPrime2048b.pkl"
    min_prime_path = "QminPrime2048b.pkl"
    p_median = (p_max + p_min)//2
    filter = lambda x: 2*x +1
    values = filter(p_min), filter(p_median), filter(p_max)
    return min_max_primes(max_path=max_prime_path,
                          min_path=min_prime_path,
                          bits=bits,
                          values=values)


def load_primes():
    p_maxPrime = load("maxPrime2048b.pkl")
    p_minPrime = load("minPrime2048b.pkl")
    q_maxPrime = load("QmaxPrime2048b.pkl")
    q_minPrime = load("QminPrime2048b.pkl")
    # print(f'P-MAX: {p_maxPrime}\nP-MIN: {p_minPrime}\n'
    #       f'{"-"*20}\n'
    #       f'Q-MAX: {q_maxPrime}\nQ-MIN: {q_minPrime}')
    return p_minPrime, p_maxPrime, q_minPrime, q_maxPrime


def isDivided(x):
    if not isCongruent(x,2,3):
        return True # Don't Use x
    for p in Primes16:
        if x%p==0:
            return True # Don't Use x
    return False

def sievingP16(p:int):
    for prime in Primes16:
        if p % prime == 0:
            return False  # Don't Use x
        if (2*p+1)%prime ==0: # Naccache check for Q
            return False # Don't Use P
    return True


def extraSievingP8(p:int):
    for prime in pPrimes8:
        if ((p-1)//2)%prime[1]==0: # Naccache
            return False # Don't Use P
        if isCongruent(p, prime[0], prime[1]):
            return False # Don't Use P
    return True



def sievingP(p:int):
    if not isCongruent(p,2,3):
        return False # Don't Use x
    # if isCongruent(p,1,3):
    #     return False # Don't Use P
    if not isCongruent(p,3,4):
        return False
    q = 2*p+1
    if not isCongruent(q,2,3):
        return False
    if not isCongruent(q,3,4):
        return False
    return extraSievingP8(p)



def random_field(min, max):
    from random import randint
    i=0
    total = (max-min)//2
    rand = lambda: randint(0,total)
    gen = lambda x: min + 2*x
    rint = rand()
    past = [rint]
    while i<total:
        yield gen(rint)
        rint = rand()
        # while rint in past:
        #     rint = rand()
        # past.append(rint)
        i += 1


def pair_finder(min,max):
    isPrime = lambda x: miller_rabin(x, 1)
    # search_field = range(min, max,2)
    search_field = random_field(min, max)
    tries = 0
    for p in search_field:
        tries +=1
        if sievingP(p):
            if sievingP16(p):
                if isPrime(p):
                    print ('*',end=' ')
                    q = 2*p+1
                    if isPrime(q):
                        print(f'\nNumber of tries: {tries}\n')
                        return p,q
    return None


def run():
    min, max,_,_ = load_primes()
    # max = 179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137215
    # min = 89884656743115795386465259539451236680898848947115328636715040578866337902750481566354238661203768010560056939935696678829394884407208311246423715319737062188883946712432742638151109800623047059726541476042502884419075341171231440736956555270413618581675255342293149119973622969239858152417678164812112068609
    # min, max = 1,101
    # max = 340282366920938463463374607431768211455 #128bits
    # min = 170141183460469231731687303715884105729 #128bits
    # max = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084095
    # min = 6703903964971298549787012499102923063739682910296196688861780721860882015036773488400937149083451713845015929093243025426876941405973284973216824503042049
    test = lambda : pair_finder(min,max)
    result = profiler(test)
    if result==None:
        print('No Pair')
    else:
        print(f'P: {result[0]}\n\nQ: {result[1]}')



if __name__=="__main__":
    print('START')
    run()
print('START')
run()
