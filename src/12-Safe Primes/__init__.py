import sys
sys.path.append('..')
from utilities import profiler, load_file as load, eratosthenes
from miller_rabin import miller_rabin
from big_primes_utilites import min_max_primes
max_prime_path = "maxPrime2048b.pkl"
min_prime_path = "minPrime2048b.pkl"
Primes16 = eratosthenes(2 ** 16)[1:]
isCongruent = lambda a, b, n: (a % n) == (b % n)
