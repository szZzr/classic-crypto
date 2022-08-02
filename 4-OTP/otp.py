def alphabet()->dict:
    abc = {chr(65+i):format(i,'05b') for i in range(26)}
    symbols = ['.','!','?','(',')','-']
    abc.update({s:format(26+i,'05b') for i,s in enumerate(symbols)})
    return abc

def numberbet()->dict:
    abc = alphabet()
    return {num:letter for letter,num in zip(abc.keys(),abc.values())}


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


def to_digit(text:str)->str:
    for letter in text:
        if ord(letter)>=48 and ord(letter)<=57:
            print(letter)
            raise ValueError('Numbers are not acceptable.')
    plain = text.replace(' ','').upper()
    abc = alphabet()
    digits = ''
    for letter in plain:
        digits += abc[letter]
    return digits


def to_char(text:str)->str:
    numbers = numberbet()
    result = ''
    for i in range(0,len(text),5):
        letter = text[i:i+5]
        result += numbers[letter]
    return result


def key(size:int)->str:
    import random
    max_bin = int('1'*size, 2)-1
    key_bin = format(random.randrange(0,max_bin+1), f'0{size}b')
    return key_bin


def en_de_cryptor(text:str, key:str)->str:
    l_text = to_list(text)
    l_key = to_list(key)
    return to_str(xor(l_text, l_key))


def show(message, key_bits, cipher_bits, plain_bits):
    print(f'Message: {message}')
    print(f'Key: {to_char(key_bits)}')
    print(f'Cipher: {to_char(cipher_bits)}')
    print(f'Plait text after decryption: {to_char(plain_bits)}')


def main(message:str):
    message_bits = to_digit(message)
    key_bits = key(len(message_bits))
    cipher_bits = en_de_cryptor(message_bits, key_bits)
    plain_bits = en_de_cryptor(cipher_bits,key_bits)
    show(message, key_bits, cipher_bits, plain_bits)



main('hello I M GIORGOS. RIZOS? WHO IS (RIZOS) --- ?')
