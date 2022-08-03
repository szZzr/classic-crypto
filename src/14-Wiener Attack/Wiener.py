import sys
sys.path.append('..')
from Wiener_Utilities import continuous_fractions as c_fractions
from Wiener_Utilities import irreducible_fractions as ir_fractions
from Wiener_Utilities import quadratic_equation_roots  as roots
from Wiener_Utilities import base64_decode as b64
from utilities import extended_euclidean,pow, decrypt_RSA as dRSA


C=[47406263192693509,51065178201172223,30260565235128704,82385963334404268,
8169156663927929,47406263192693509,178275977336696442,134434295894803806,
112111571835512307,119391151761050882,30260565235128704,82385963334404268,
134434295894803806,47406263192693509,45815320972560202,174632229312041248,
30260565235128704,47406263192693509,119391151761050882,57208077766585306,
134434295894803806,47406263192693509,119391151761050882,47406263192693509,
112111571835512307,52882851026072507,119391151761050882,57208077766585306,
119391151761050882,112111571835512307,8169156663927929,134434295894803806,
57208077766585306,47406263192693509,185582105275050932,174632229312041248,
134434295894803806,82385963334404268,172565386393443624,106356501893546401,
8169156663927929,47406263192693509,10361059720610816,134434295894803806,
119391151761050882,172565386393443624,47406263192693509,8169156663927929,
52882851026072507,119391151761050882,8169156663927929,47406263192693509,
45815320972560202,174632229312041248,30260565235128704,47406263192693509,
52882851026072507,119391151761050882,111523408212481879,134434295894803806,
47406263192693509,112111571835512307,52882851026072507,119391151761050882,
57208077766585306,119391151761050882,112111571835512307,8169156663927929,
134434295894803806,57208077766585306]

def is_int(number):
    return float(number).is_integer()


def Wiener(N:int, e:int):
    n = 15
    cfracs = c_fractions(e/N, bound=n)
    N_D = []
    Phi = []
    for i in range(n):
        ND = ir_fractions(cfracs[:i+2])
        N_D.append(ND)
        Phi.append((e*ND[1]-1)//ND[0])
    print(f'e-N: {cfracs}\n\nNi-Di: {N_D}\n\nPhi: {Phi}')
    for i in range(1,n):
        if is_int(Phi[i]):
            reals, x1, x2 = roots([1,-(N - Phi[i] +1), N])
            if reals:
                if is_int(x1) & is_int(x2):
                    return (int(x1), int(x2))
    print('FAIL')
    return None


def eval_Wiener():
    N = 5697733
    e = 3105251
    result = Wiener(N,e)
    if result != None:
        print(f'p: {result[0]}\t q:{result[1]}')
        if result == (2393, 2381):
            print('Evaluated!!!')


def get_n_e(text):
    acceptable_char = lambda char: ord(char) in range(48,58)
    new_text = []
    text = text.split(' ')
    for word in text:
        to_remove = []
        for char in word:
            if not acceptable_char(char):
                to_remove.append(char)
        for char in to_remove:
            word = word.replace(char,'')
        new_text.append(word)
    return new_text[-2], new_text[-1]


def load_file(path):
    with open(path, 'r') as file:
        data = file.read()
    data = data.split('\n')
    data = list(filter(None, data))
    N,e = get_n_e(data[0])
    cipher = b64(data[1])
    print(f'N: {N}\te: {e}\ncipher: {cipher}')
    return int(N), int(e), cipher


def decrypt(p,q,e,cipher):
    phi = (p-1)*(q-1)
    d = extended_euclidean(e, phi)[0]
    print(f'd: {d}')
    message = [chr(c) for c in dRSA(cipher=cipher, d=d,N=p*q)]
    print(f'message: {"".join(message)}')

def run_Wienner(path = 'cipher_rsa.txt'):
    N, e , cipher = load_file(path)
    result = Wiener(N, e)
    if result != None:
        p,q = result
        print(f'p: {p}\t q:{q}')
        decrypt(p,q,e,C)





# eval_Wiener()
run_Wienner()


