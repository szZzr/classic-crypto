import sys
sys.path.append('..')
from utilities import pow, karatsuba as karatsuba_multiplication, profiler

def traditional_multiplication(number1,number2):
    _a_ = [int(i) for i in str(number1)]
    _b_ = [int(i) for i in str(number2)]
    _a_.reverse()
    _b_.reverse()
    result = 0
    for i,b in enumerate(_b_):
        in_result = 0
        for j,a in enumerate(_a_):
            in_result += a*b*(10**j)
        result += in_result*(10**i)
    return result



def solve(multiplication):
    a = pow(2,1000)
    b = pow(3,101)
    c = pow(5,47)
    p = pow(2,107)-1
    # return (a*b*c)%p
    # print(f'a = {a}\nb = {b}\nc = {c}')
    return multiplication(multiplication(a,b), c)%p


def comparison():
    a = pow(3,12345)
    b = pow(5,12345)
    print(a,b)
    karatsuba = lambda:karatsuba_multiplication(a,b)
    traditional = lambda: traditional_multiplication(a,b)

    profiler(karatsuba)
    profiler(traditional)

# solve(karatsuba_multiplication)
test = lambda : solve(karatsuba_multiplication)
result = profiler(test)
print(f'2^100 * 3^101 * 5^47 (mod 2^107 - 1) = {result}')

# comparison()
