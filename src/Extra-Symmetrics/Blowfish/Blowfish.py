def CBC_Blowfish_encyptor(text,key,IV):
    '''
    encrypt a plain text with blowfish encryption in CBC mode
    :param text: plain text
    :param key: key for encryption
    :param IV: Initialization Vector
    :return: cipher text
    '''
    from Crypto.Cipher import Blowfish
    mode = Blowfish.MODE_CBC
    encryptor = Blowfish.new(key,mode,IV)
    ciphertext = encryptor.encrypt(text)
    return ciphertext


def CBC_Blowfish_decryptor(text,key,IV):
    '''
    decrypt cipher text with blowfish encryption in CBC mode
    :param text: plain text
    :param key: key for encryption
    :param IV: Initialization Vector
    :return: plain text
    '''
    from Crypto.Cipher import Blowfish
    mode = Blowfish.MODE_CBC
    decryptor = Blowfish.new(key,mode,IV)
    plaintext = decryptor.decrypt(text)
    return plaintext

def CBC_texts_encryption(data,key,IV):
    '''
    get data and encrypt with blowfish crypto in CBC mode
    :param data: pairs of plain texts with 1 bit difference data[pairs][0]-> original txt, data[pairs][2]-> 1bit diff
    :param key: key for encryption
    :param IV: Initialization Vector
    :return: UPDATE list with cipher data in data[pairs][1]-> original cipher txt, data[pairs][3] -> 1bit diff cipher txt
    '''
    for i in range(len(data)):
        plaintxt = data[i]
        plaintxt1 = ''.join(plaintxt[0]) # plain mess1 data[pairs][0]
        if len(plaintxt1)%8 != 0: # to be multiply by 8
            plaintxt1 = plaintxt1 + (8-(len(plaintxt1)%8))*'0'
        plaintxt2 = ''.join(plaintxt[3]) # plain mess1 data[pairs][3]
        if len(plaintxt2)%8 != 0: # to be multiply by 8
            plaintxt2 = plaintxt2 + (8-(len(plaintxt2)%8))*'0'
        data[i][1] = CBC_Blowfish_encyptor(plaintxt1,key,IV)
        data[i][4] = CBC_Blowfish_encyptor(plaintxt2,key,IV)
    return data # Update data list


def CBC_texts_decryption(cipherdata,key,IV):
    '''
    get cipher data and decrypt for blowfish crypto in CBC mode
    :param data: pairs of plain texts with 1 bit difference data[pairs][1]-> original txt, data[pairs][3]-> 1bit diff
    :param key: key for encryption
    :param IV: Initialization Vector
    :return: NEW list with decrypted data at data[pairs][0]-->original txt data[pairs][1]--> 1bit diff txt
    '''
    data = [[[] for k in range(2)] for i in range(len(cipherdata))]
    for i in range(len(data)):
        ciphertxt = cipherdata[i]
        ciphertxt1 = ciphertxt[1]
        ciphertxt2 = ciphertxt[4]
        data[i][0] = CBC_Blowfish_decryptor(ciphertxt1,key,IV)
        data[i][1] = CBC_Blowfish_decryptor(ciphertxt2,key,IV)
    return data # New list


def ECB_Blowfish_encyptor(text,key):
    '''
    encrypt a plain text with blowfish encryption in ECB mode
    :param text: plain text
    :param key: key for encryption
    :return: cipher text
    '''
    from Crypto.Cipher import Blowfish
    mode = Blowfish.MODE_ECB
    encryptor = Blowfish.new(key,mode)
    ciphertext = encryptor.encrypt(text)
    return ciphertext


def ECB_Blowfish_decryptor(text,key):
    '''
    decrypt cipher text with blowfish encryption in ECB mode
    :param text: plain text
    :param key: key for encryption
    :return: plain text
    '''
    from Crypto.Cipher import Blowfish
    mode = Blowfish.MODE_ECB
    decryptor = Blowfish.new(key,mode)
    plaintext = decryptor.decrypt(text)
    return plaintext


def ECB_texts_encryption(data,key):
    '''
    get data and encrypt with blowfish crypto in ECB mode
    :param data: pairs of plain texts with 1 bit difference data[pairs][0]-> original txt, data[pairs][2]-> 1bit diff
    :param key: key for encryption
    :return: UPDATE list with cipher data in data[pairs][1]-> original cipher txt, data[pairs][3] -> 1bit diff cipher txt
    '''
    for i in range(len(data)):
        plaintxt = data[i]
        plaintxt1 = ''.join(plaintxt[0]) # plain mess1 data[pairs][0]
        if len(plaintxt1)%8 != 0: # to be multiply by 8
            plaintxt1 = plaintxt1 + (8-(len(plaintxt1)%8))*'0'
        plaintxt2 = ''.join(plaintxt[3]) # plain mess1 data[pairs][3]
        if len(plaintxt2)%8 != 0: # to be multiply by 8
            plaintxt2 = plaintxt2 + (8-(len(plaintxt2)%8))*'0'
        data[i][2] = ECB_Blowfish_encyptor(plaintxt1,key)
        data[i][5] = ECB_Blowfish_encyptor(plaintxt2,key)
    return data # Update data list


def ECB_texts_decryption(cipherdata,key):
    '''
    get cipher data and decrypt for blowfish crypto in ECB mode
    :param data: pairs of plain texts with 1 bit difference data[pairs][1]-> original txt, data[pairs][3]-> 1bit diff
    :param key: key for encryption
    :return: NEW list with decrypted data at data[pairs][0]-->original txt data[pairs][1]--> 1bit diff txt
    '''
    data = [[[] for k in range(6)] for i in range(len(cipherdata))]
    for i in range(len(data)):
        ciphertxt = cipherdata[i]
        ciphertxt1 = ciphertxt[2] # ECB cipher mess1 data[pairs][2]
        ciphertxt2 = ciphertxt[5] # ECB cipher mess2 data[pairs][2]
        data[i][0] = ECB_Blowfish_decryptor(ciphertxt1,key)
        data[i][2] = ECB_Blowfish_decryptor(ciphertxt2,key)
    return data # New list

def text_generator(pairs):
    '''
    data generator
    produce random length messages with 1 bit difference
    random(65,90)==random(A,Z) text content
    random bit for change
    :param pairs: number of message pairs with 1 bit differnce
    :return: new data
    '''
    import random
    textlist = [[0 for k in range(8)] for i in range(pairs)]
    for i in range(pairs):
        lentxt = random.randint(30,100+i) # random length
        lentxt += lentxt%8
        m1 = [bin(random.randint(65,90)) for i in range(lentxt)] # random binaries generator
        m2 = m1.copy() # duplicate m1 to change a bit
        randindex = random.randint(0, len(m2[0])-1) # random byte
        temp = m2[randindex]
        temp = list(temp)
        brandindex = random.randint(2,len(temp)-1) # random bit's index
        b = temp[brandindex]
        b = int(b) # bit convert to int for change
        b ^= 1 # change bit
        b = str(b) # bit convert to string
        temp[brandindex] = b # insert to list
        temp = ''.join(temp) # convert list to sting
        m2[randindex] = temp
        textlist[i][0]=m1 # data[pair][0] -> message No1
        textlist[i][3]=m2 # data[pair][3] -> message No2
    return textlist # return data


def avalanche_strict(data):
    '''
    calculate strict avalanche effect for CBC & ECB mode in data[pairs][6] & data[pairs][7]
    :param data: encrypted data
    :return: UPDATE data list with frequencies of non-change bits
    '''
    for i in range(len(data)): # for all encrypted messages pairs
        for k in range(len(data[i][1])):
            if data[i][1][k]==data[i][4][k]: # CBC mode
                data[i][6]+=1 # count same bits
            if data[i][2][k]==data[i][5][k]: # ECB mode
                data[i][7]+=1 # count same bits
    for i in range(len(data)):
        data[i][6] = round(data[i][6] / len(data[i][1]),3)*100 # frequency calculate CBC mode
        data[i][7] = round(data[i][7] / len(data[i][2]),3)*100 # frequency calculate ECB mode
    return data # Update data


'''
---MY DATA---
data[pair][0] -> message No1
data[pair][1] -> message No1 encrypted with Blowfish CBC
data[pair][2] -> message No1 encrypted with Blowfish ECB
data[pair][3] -> message No2
data[pair][4] -> message No2 (like mess1 with 1bit diff) encrypted with Blowfish CBC
data[pair][5] -> message No2 (like mess1 with 1bit diff) encrypted with Blowfish ECB
data[pair][6] -> avalanche effect for Blowfish CBC
data[pair][7] -> avalanche effect for Blowfish ECB

CBC_texts_encryption
CBC_texts_decryption
ECB_texts_encryption
ECB_texts_decryption
text_production
avalanche_strict
'''


data = text_generator(30)
CBC_texts_encryption(data,'123456789abcdef',8*'\x00')
ECB_texts_encryption(data,'123456789abcdef')
avalanche_strict(data)

dif = []
sum = 0 #for average computation
for i in range(len(data)):
    print('\t\t----',i+1,'----')
    print('Length m1-m2: ',len(data[i][0]))#,'\tLEN m2: ',len(data[i][3])
    print('lenCBC m1: ',len(data[i][1]),'\tlenCBC m2: ',len(data[i][4]))
    print('lenECB m1: ',len(data[i][2]),'\tlenECB m2: ',len(data[i][5]))
    print('\tAvalanche Effect -CBC- : ',data[i][6])
    print('\tAvalanche Effect -ECB- : ',data[i][7],'\n')
    thedif = abs(data[i][6]-data[i][7])
    sum+=thedif
    dif.append(thedif)
    print('The difference is: ',thedif,'%\n\n\n')

print(48*'-')
print('The average difference for 30couples is\t',round(sum/30,2),'%')
print(48*'-')
