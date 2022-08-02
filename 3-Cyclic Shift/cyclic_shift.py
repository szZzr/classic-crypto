def xor(x:list, y:list)->list:
    if len(x) != len(y):
        raise ValueError
    result = [0]*len(x)
    for i,res in enumerate(zip(x, y)):
        result[i] = res[0] ^ res[1]
    return result


def xor_args(*args)->list:
    for arg in args[1:]:
        if len(args[0]) != len(arg):
            raise ValueError
    result = [0]*len(args[0])
    for arg  in args:
        result = xor(result, arg)
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


def cyclic_shift(x:list, bits:int)->list:
    '''
    Shift cyclic left the given number of bits of
    the binary number x
    :param x: List of binary number
    :param bits: Integer to shift
    :return:
    '''
    return x[bits:] + x[:bits]


def encryption(message:str)->list:
    '''
    cipher = msg XOR msg<<6 XOR msg<<10
    :param message:
    :return: List with cipher
    '''
    msg = to_list(message)
    msg6 = cyclic_shift(msg,6)
    msg10 = cyclic_shift(msg,10)
    return xor_args(msg, msg10, msg6)


def decryption(cipher:list)->list:
    '''
    Decrypt the given cipher text. Just with inputs og 16bits.
    :param cipher:
    :return:
    '''
    if len(cipher)!=16:
        raise ValueError
    msg = [0]*16
    y = xor_args(cipher[4:8], cipher[10:14], cipher[2:6], cipher[8:12], cipher[6:10])
    m = xor_args(cipher[0:4], cipher[10:14], y)
    t  = xor_args(cipher[2:6], cipher[12:16], y)
    msg[:2] = xor_args(t[2:], y[:2], cipher[:2])
    msg[12:14] = xor_args(y[:2], cipher[6:8], msg[:2])
    msg[2:4] = xor_args(y[:2], cipher[12:14], msg[12:14])
    msg[14:16] = xor_args(t[2:], m[:2], cipher[4:6])
    msg[4:12] = m + t
    return msg


def to_str(list_int:list)->str:
    '''
    Convert a list with integers to string
    :param list_int: List with integers
    :return: String
    '''
    return ''.join([str(l) for l in list_int])


def main(message:str)->None:
    cipher = encryption(message)
    plain = decryption(cipher)
    print(f'message: {message}\ncipher: {to_str(cipher)}\nplain: {to_str(plain)}')
    print(f'\nPlain == Message => {message == to_str(plain)}')


main(message = '1101011011101110')
