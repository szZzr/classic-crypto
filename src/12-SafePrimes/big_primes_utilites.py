import sys
sys.path.append('..')
from miller_rabin import miller_rabin
from utilities import save_file as save

def prime_finder(search_field:range):
    isPrime = lambda x: miller_rabin(x, 1)
    for i in search_field:
        # print(f'number: {i}\n\n')
        if isPrime(i):
            return i
    return 0


def max_prime(median:int, max:int)->int:
    search_field = range(max,median-1,-2)
    # print(f'max-search-field: {search_field}')
    return prime_finder(search_field)


def min_prime(median:int, min:int)->int:
    search_field = range(min, median+1, 2)
    # print(f'min-search-field: {search_field}')
    return prime_finder(search_field)

def save_prime(prime, path, content:str=''):
    print(f'{content} Prime: {prime}')
    save(data=prime, path=path)

def standar_values(bits:int=2048):
    max_bin = '1' * bits
    max = int(max_bin, 2)
    min_bin = '1' + '0' * (bits - 1)
    min = int(min_bin, 2)
    median = (max+min)//2
    if min%2==0:
        min+=1
    if max%2==0:
        max-=1
    return min, median, max


def find_max_prime(path:str, new_values=None, bits:int=2048):
    '''
    Brute force method to reveal the maximum primitive
    number of given size of bits (default size 2048 bits).
    This method find the number and save it in a file.
    and save it in file.
    :return: Max primitive of given size
    '''
    _, median, max = standar_values(bits) if new_values==None  else new_values
    if median%2==0:
        median-=1
    maxPrime = max_prime(median=median, max = max)
    save_prime(prime=maxPrime, path=path, content='Max')
    return maxPrime


def find_min_prime(path:str, new_values=None, bits:int=2048):
    '''
    Brute force method to reveal the maximum primitive
    number of given size of bits (default size 2048 bits).
    This method find the number and save it in a file.
    and save it in file.
    :return: Max primitive of given size
    '''
    min, median, _ = standar_values(bits) if new_values==None else new_values
    if median%2==0:
        median+=1
    minPrime = min_prime(min=min, median=median) # +1 because min is an even number
    save_prime(prime=minPrime, path=path, content='Min')
    return minPrime





def min_max_primes(max_path:str, min_path:str, values=None, bits:int=2048):
    maxPrime =  find_max_prime(path=max_path, bits=bits, new_values=values)
    minPrime = find_min_prime(path=min_path, bits=bits, new_values=values)
    return maxPrime,minPrime






