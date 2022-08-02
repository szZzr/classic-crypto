import sys
sys.path.append("..")
from utilities import pow, decrypt_RSA as decrypt

C = [ 3203, 909, 3143, 5255, 5343, 3203, 909, 9958, 5278, 5343,
      9958,5278, 4674, 909, 9958, 792, 909, 4132, 3143, 9958, 3203, 5343, 792, 3143, 4443]



def toASCII(encoded):
    decoded = [chr(char) for char in encoded]
    return ''.join(decoded)

d = 1179
N = 11413


message = toASCII(decrypt(C,d,N))
print(f'Cipher: {C}\n\nMessage: {message}')
