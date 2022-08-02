import sys
sys.path.append('..')
from utilities import fibonacci, profiler
from miller_rabin import miller_rabin

def run_fib_is_prime(fib_index:int, repeats:int):
    print(f'Prime Search for Fibonacci({fib_index})')
    print(f'Number of evaluation {repeats}-times.\n')
    fib = fibonacci(fib_index)
    test  = lambda: miller_rabin(fib, 4)
    isPrime = profiler(test)
    if isPrime:
        result = '*** PRIME ***'
    else:
        result = '-> NoN-PRIME <-'
    print(f'Test Result: \t{result}')
    print(f'Approved {repeats}-times')


run_fib_is_prime(fib_index=104911,
                 repeats=4)
