def alphabet()->dict:
    abc = {chr(65+i):i for i in range(26)}
    symbols = ['.','!','?','(',')','-']
    abc.update({s:i+26 for i,s in enumerate(symbols)})
    return abc

def numberbet()->dict:
    abc = alphabet()
    return {num:letter for letter,num in zip(abc.keys(),abc.values())}

def to_digit(text:str)->list:
    for letter in text:
        if ord(letter)>=48 and ord(letter)<=57:
            print(letter)
            raise ValueError('Numbers are not acceptable.')
    plain = text.replace(' ','').upper()
    abc = alphabet()
    digits = []
    for letter in plain:
        digits.append(abc[letter])
    return digits

def to_char(text:str)->str:
    numbers = numberbet()
    result = ''
    for letter in text:
        result += numbers[letter]
    return result

def dec(bbytes:bytes):
    return int.from_bytes(bbytes,'big')

def bytes(integer:int):
    return (integer).to_bytes(1,'big')


def shift(seed:list):
    seedlen = len(seed)
    S = [i for i in range(32)]
    j = 0
    for i in range(32):
        j = (j + S[i] + seed[i%seedlen] ) % 32
        S[i], S[j] = S[j], S[i]
    return S


def cipher_rc4(S:list, message:list):
    key = []
    j = 0
    for l in range(len(message)):
        i = l%32
        j = (j + S[i])%32
        S[i], S[j] = S[j], S[i]
        key.append(S[(S[i]+ S[j])%32])
    return key


def en_de_cryptor(text:list, kkey:list)->list:
    s = shift(kkey)
    key = cipher_rc4(s,text)
    return [t^k for t,k in zip(text,key)]


def show(message, key_bits, cipher_bits, plain_bits):
    print(f'Message: {message}')
    print(f'Key: {to_char(key_bits)}')
    print(f'Cipher: {to_char(cipher_bits)}')
    print(f'Plait text after decryption: {to_char(plain_bits)}')


def main(message:str, kkey:str):
    msg_b = to_digit(message)
    key_b = to_digit(kkey)
    cipher_b = en_de_cryptor(msg_b, key_b)
    plain_b = en_de_cryptor(cipher_b, key_b)
    show(message, key_b, cipher_b, plain_b)


message = 'MISTAKES ARE AS SERIOUS AS THE RESULTS THEY CAUSE'
key = 'HOUSE'
main(message,key)
