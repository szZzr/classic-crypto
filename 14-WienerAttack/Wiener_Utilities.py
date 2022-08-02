import sys
sys.path.append('..')
from utilities import lcm, euclidean

def continuous_fractions(x, bound):
    factors = [int(x)]
    i = 0
    x = x - factors[i]
    while x>0:
        i +=1
        factors.append(int(1/x))
        x = 1/x - factors[i]
        if i>=bound:
            return factors
    return factors

def test_continuous_fractions():
    cfract = continuous_fractions(3105251/5697733)
    print(cfract)


def irreducible_number(c_fract:list):
    n = len(c_fract)-1
    result = 0
    for i in range(n,0,-1):
        result = 1/(result+c_fract[i])
    return result+c_fract[0]


def tradition_fractions_add(x:tuple,y:tuple)->tuple:
    '''
    Estimates the summary of two fractions, and returns
    a fraction. The first argument of tuple denotes the
    numerator and the second the denominator.
    :param x: first fraction tuple
    :param y: second fraction tuple
    :return: fraction as sum of fractions
    '''
    denominator = lcm(x[1],y[1])
    x0 = (denominator/x[1])*x[0]
    y0 = (denominator/y[1])*y[0]
    z0 = x0 + y0
    gcd  = euclidean(z0,denominator)
    return (int(z0/gcd), int(denominator/gcd))


def swap_tuple(t:tuple):
    '''
    Set the denominator as numerator and vice versa
    for numerator. In fact, the input is a fraction,
    so this method divides 1 by the input fraction and
    returns a fraction.
    :param t: Fraction as tuple.
    :return:
    '''
    return (t[1],t[0])


def irreducible_fractions(c_fract:list):
    '''
    Take as argument a list with arguments of a continuous
    fraction and estimates the irreducible fraction. The numerator
    represent the N_i and the denominator denotes the e_i
    :param c_fract: List of arguments of a continuous fraction
    :return: Fraction as a tuple (numerator,denominator)
    '''
    n = len(c_fract)
    if n<2:
        return None
    ir_fractions = (1,c_fract[-1])
    for i in range(n-2,0,-1):
        fraction = tradition_fractions_add( ir_fractions, (c_fract[i],1))
        ir_fractions = swap_tuple(fraction)
    ir_fractions = tradition_fractions_add(ir_fractions, (c_fract[0], 1))
    return ir_fractions


def quadratic_equation_roots(args:list):
    '''
    Estimates the Real roots of a second degree polynomial.
    If the roots are complex numbers return False otherwise if
    are real numbers return True and
    :param args: List with polynomial coefficients.
    :return: areReal, Root1, Root2
    '''
    from math import sqrt
    discriminant = args[1]**2 - 4 * args[0] * args[2]
    if discriminant<0:
        return False, None, None
    root1 = (-args[1] + sqrt(discriminant))/2*args[0]
    if discriminant==0:
        return True, root1, root1
    root2 = (-args[1] - sqrt(discriminant))/2*args[0]
    return True, root1, root2


def base64_decode(encoded_text):
    '''
    Decode a base64 encoded text.
    :param encoded_text: Encoded Text
    :return: Text
    '''
    import base64
    b64_bytes = encoded_text.encode("ascii")
    bytes_string = base64.b64decode(b64_bytes)
    return bytes_string.decode("ascii")

