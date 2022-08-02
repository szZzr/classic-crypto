abc = [chr(letter) for letter in range(945, 970)]
abc.pop(17)

def digitalizer(text:str)->list:
    return [abc.index(letter)+1 for letter in text]


def characterizer(digital:list)->list:
    return [abc[number-1] for number in digital]

def decryption(digital,x):
    return [(number+x)%25 + (number+x>24) for number in digital]

def main(key:int):
    cipher = 'οκηθμφδζθγοθχυκχσφθμφμχγ'
    digital = digitalizer(cipher)
    decrypt = decryption(digital,key)
    plain_text = characterizer(decrypt)
    print(''.join(plain_text).upper())

main(key=-3)





