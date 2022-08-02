import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter


sbox = np.array([
    [0,2,3,7,9,12,15,7,6,15,15,1,7,3,1,0],
    [1,5,6,13,4,1,5,11,7,8,7,1,1,3,2,13],
    [5,3,5,12,11,1,1,5,13,0,15,7,2,2,13,0],
    [3,12,3,11,2,2,2,4,6,5,5,0,4,3,1,0]])


def to_str(list_int:list)->str:
    '''
    Convert a list with integers to string
    :param list_int: List with integers
    :return: String
    '''
    return ''.join([str(l) for l in list_int])


def xor(x:list, y:list)->list:
    if len(x) != len(y):
        raise ValueError
    result = [0]*len(x)
    for i,res in enumerate(zip(x, y)):
        result[i] = res[0] ^ res[1]
    return result

def to_list(string:str)->list:
    '''
    Converts the given string of binary number,
    to list with integers-binaries.
    :param string:
    :return:
    '''
    result = [0]*len(string)
    for i,letter in enumerate(string):
        result[i] = int(letter)
    return result


def feistel(binary:str,m:int)->str:
    x = int(binary[0]+binary[-1],2)
    y = int(binary[1:-1],2)
    return format(sbox[x][y], f'0{m}b')


def analysis(n:int, m:int):
    max = int('1'*n,2) + 1
    results = {i:0 for i in range(16)}
    for i in range(1,max):
        binary = format(i,f'0{n}b')
        results[int(feistel(binary,m),2)] += 1
    return results


def diff_calc(x:str,z:str, m:int)->int:
    s1 = feistel(to_str(xor(to_list(z),to_list(x))), m)
    s2 = feistel(z, m)
    y = xor(to_list(s1),to_list(s2))
    return int(to_str(y),2)


def diff_run(n:int, m:int):
    max_val = int('1' * n, 2) + 1
    results = []
    summarize = {i: 0 for i in range(16)}
    for x in range(1,max_val):
        bin_x = format(x, f'0{n}b')
        for z in range(0,max_val):
            bin_z = format(z, f'0{n}b')
            res = diff_calc(bin_x,bin_z,m)
            results.append(res)
            summarize[res] += 1
    return results,summarize # max(results)

def plotting(data_x:list, data_y:list, name:str=''):
    plt.plot(data_x,data_y,'o-')
    plt.xlabel("S-Box Values")
    plt.ylabel("Times")
    plt.title(f"Differential Uniform {name}")
    plt.show()


def main():
    results = analysis(n=6, m=4)
    plotting(list(results.keys()), list(results.values()),name='S(x)')

    l, d = diff_run(6,4)
    plotting(list(d.keys()), list(d.values()),name='S(z xor x) xor S(z)')


main()
