from Cryptodome.Cipher import AES
import random, numpy as np

def encryptor_aes(key:bytes, data:bytes, mode:AES):
    cipher = AES.new(key, mode)
    ciphertxt = cipher.encrypt(data)
    return ciphertxt


def decryptor_aes(key:bytes, ciphertxt:bytes, mode:AES):
    cipher = AES.new(key, mode)
    plaintext = cipher.decrypt(ciphertxt)
    return plaintext


def key_generator(bits_size:int)->str:
    max_bin = int('1'*bits_size, 2)-1
    return format(random.randrange(0,max_bin+1), f'0{bits_size}b')


def message_generator(bits_size:int)->(str,str):
    max = int('1'*bits_size,2)
    msg1 = format(random.randrange(0,max+1), f'0{bits_size}b')
    msg2 = list(msg1)
    index = random.randrange(0,255)
    msg2[index] = int(msg2[index])^1
    to_str = lambda llist: ''.join([str(l) for l in llist])
    return msg1, to_str(msg2)


def to_bytes(binary:str)->bytes:
    return int(binary,2).to_bytes(len(binary)//8,'big')


def to_bin(bbytes:bytes,bits_size:int)->str:
    dec = int.from_bytes(bbytes,'big')
    return format(dec, f'0{bits_size}b')


def bits_comparison(bin1:str, bin2:str)->int:
    diff = 0
    for b1,b2 in zip(bin1,bin2):
        diff += b1!=b2
    return diff


def avalanche_effect(size:int, mode:AES)->np.ndarray:
    results = np.zeros(100, dtype=int)
    for i in range(100):
        key = key_generator(16*8)
        m1, m2 = message_generator(size)
        en1 = encryptor_aes(to_bytes(key), to_bytes(m1), mode)
        en2 = encryptor_aes(to_bytes(key), to_bytes(m2), mode)
        results[i] = bits_comparison(to_bin(en1, size), to_bin(en2,size))
    return results


cbc = avalanche_effect(256, AES.MODE_CBC)
ecb = avalanche_effect(256, AES.MODE_ECB)
print(f'CBC: {int(np.average(cbc))}\nECB: {int(np.average(ecb))}')
