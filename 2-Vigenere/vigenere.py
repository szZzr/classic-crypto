import sys
sys.path.append('.')
from support import *

'''
VIGENERE
'''
def encryptor(plain, key):
    cipher = []
    for k,p in zip(key, plain):
        cipher.append(
            (k+p)%27 + ((k+p)>26))
    return cipher


def reveal_pssw(cipher:str, plain:str):
    key = []
    for c,p in zip(cipher,plain):
        key.append(digitalizer(c)[0] - digitalizer(p)[0])
    return characterizer(key)



def decryptor(cipher:str,key:str)->str:
    plain = []
    c = 0
    for letter in cipher:
        plain.append(
            digitalizer(letter)[0] - digitalizer(key[c])[0]
        )
        c = 0 if c+1>=len(key) else c+1
    return ''.join(characterizer(plain))


key = 'SHANNON'
plain = decryptor(cipher_2, key)
print(f'Cipher-Text: {cipher_2}\nKey: {key}\nPlain-Text: {plain}')
