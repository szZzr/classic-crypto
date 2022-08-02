def alphabet ():
    '''
    Dictionary creator for alphabet with 5bit-code
    :return: dictionary
    '''
    ab=[]
    bin_ab=[]
    for i in range(32):
        temp = format(i,'b')
        temp = (5-len(temp))*'0'+temp
        bin_ab.append(temp)
    for i in range(65,65+26):
        ab.append(chr(i))
    ab.append('.')
    ab.append('!')
    ab.append('?')
    ab.append('(')
    ab.append(')')
    ab.append('-')
    my_alphabet = {ab[x]:bin_ab[x] for x in range(len(ab))}
    return my_alphabet


def txt_dec(stream):
    ab = alphabet()
    ab_keys = list(ab.keys())
    ab_values = list(ab.values())
    ab_finder = {ab_values[x]:ab_keys[x] for x in range(len(ab_keys))}
    decrypted_text = []
    for bits in stream:
        decrypted_text.append(ab_finder.get(''.join(bits)))
    return decrypted_text


def keystream_finder(msg,encr):
    msg = msg.upper()
    encr = encr.upper()
    ab = alphabet()
    bin_msg = ab.get(msg[0])+ab.get(msg[1])
    bin_encr = ab.get(encr[0])+ab.get(encr[1])
    bin_key=[]
    for i in range(10):
        bin_key.append(int(bin_msg[i]) ^ int(bin_encr[i]))
    # my_keystream = ''.join(bin_key)
    return bin_key


def fb_table_creator(fbfunc):
    table = []
    table.append(fbfunc)
    for i in range(1,10):
        row = [0 for i in range(10)]
        row[i-1] = 1
        table.append(row)
    return table


def array_multiplier(t1,t2):
    import numpy
    x = numpy.matmul(t1,t2)
    x = numpy.mod(x,2)
    x = x.tolist()
    return x
    #myAlgo for matrix multiply
    # try:
    #     if(len(t1[0]) == len(t2)):
    #         if(isinstance(t2[0],list)):
    #             result = [[0 for i in range(len(t2[0]))] for k in range(len(t2))]
    #             for row in range(len(result)):
    #                 for column in range(len(result[0])):
    #                     for loop in range(len(result)):
    #                         result[row][column] = (t1[row][loop] * t2[loop][column] + result[row][column])%2
    #         else:
    #             result = [0 for i in range(len(t2))]
    #             for i in range(len(result)):
    #                 for j in range(len(t1[0])):
    #                     result[i]= (result[i]+ t1[i][j]*t2[j])%2
    #         return result
    # except TypeError:
    #     return False


def inv_matrix(matrix):
    import numpy
    if(numpy.linalg.det(matrix)!=0):
        x = numpy.linalg.inv(matrix)
        x = x.astype(int)
        x = x.tolist()
        return x
    else:
        return False


def read_txt(path):
    '''
    read the encrypted txt file with greek encoding mac_greek
    :param path: of the txt file
    :return: bit-list of encrypted txt file
    '''
    import codecs
    with codecs.open(path, 'r') as f:
        txt = list(f.read())
    txt = txt[1:len(txt)-2]
    ab = alphabet()
    stream = []
    for i in txt:
        stream.append(ab.get(i.upper()))
    return bits_to_bit(stream)

def bits_to_bit(stream):
    '''
    Break the 5bit group to bit list
    :param stream: list with 5bit groups
    :return: bit list
    '''
    bstream = []
    for bits in stream:
        for b in bits:
            bstream.append(int(b))
    return bstream


def bit_to_bits(stream):
    '''
    Group bit_list to 5bit_list composed of string
    :param stream: list of bits
    :return: string list of 5bits group
    '''
    bstream = []
    l=0
    string= ''
    for b in stream:
        string = string + str(b)
        l+=1
        if(l==5):
            bstream.append(string)
            string=''
            l=0
    return bstream

def prg_lfsr(feed_back_func,seed,nbits):
    '''
    LFSR-10bit PRG implementation... generator of keystream
    :param feed_back_func: the feed back function fo lfsr
    :param seed: lfsr's seed
    :param nbits: bits's number of message
    :return: bit-list with the message's key stream
    '''
    keystream = []
    c = fb_table_creator(feed_back_func)
    x = seed
    loops = int(nbits/10)
    for i in range(loops):
        x = array_multiplier(c,x)
        keystream.append(x)
    return bits_to_bit(keystream)


def lfsr_dec(keystream,cipher):
    decrypted = [] #binary decrypted list of bits xor
    for i in range(len(cipher)):
        decrypted.append(cipher[i]^keystream[i])
    decrypted_bin_text = bit_to_bits(decrypted) #group bit_list to 5bit_list
    return txt_dec(decrypted_bin_text)


def seed_finder(keystream):
    r_keystream = keystream[::-1] #reverse keystream
    for i in range(len(keystream)):
        f = r_keystream[0]^r_keystream[6]^r_keystream[7]^r_keystream[9] #feedback function for previous
        r_keystream = r_keystream[1:10]
        r_keystream.append(f)
    return r_keystream

def PRG(seed,ffunc,msg_bits):
    lfsr = []
    c = fb_table_creator(ffunc)
    for i in range(msg_bits):
        lfsr.append(seed[len(seed)-1])
        seed = array_multiplier(c,seed)
    return lfsr



feedbackfunc = [0,0,0,0,0,1,1,0,1,1] #the feedback function x^10+x^9+x^7+x^6+1
keystream = list(keystream_finder('ab','sq')) #key finder xor('ab','sq')


path = '/Users/rizos/Desktop/lfsr.txt'
cipher = read_txt(path)

seed = seed_finder(keystream)
lfsr = PRG(seed,feedbackfunc,len(cipher))
msg = lfsr_dec(lfsr,cipher)

print('Keystream \'ab\' and \'sq\':\t',str(keystream),'\n')
print('Seed:\t', str(seed))
print('\n\nThe message:\t',''.join(msg))




# FIRST TRY!!!
# feedbackfunc = [0,0,0,0,0,1,1,0,1,1] #the feedback function x^10+x^9+x^7+x^6+1
# keystream = list(keystream_finder('ab','sq')) #key finder xor('ab','sq')
# print('Keystream \'ab\' and \'sq\':'  , keystream)
# c = fb_table_creator(feedbackfunc) #create matrix for feedbackfunction
# cinv = inv_matrix(c)
# c2 = array_multiplier(c,c) #matrix^2
# c2inv = inv_matrix(c2) #inverse the matrix^2
# if(c2inv!=False):
#     seed = array_multiplier(cinv,key_ab) #seed: multiply inverse-matrix^2 and keystream
#     print('\nMy seed: ', seed)
# path = '/Users/rizos/Desktop/lfsr.txt'
# cipher = read_txt(path)
# key = prg_lfsr(feedbackfunc,seed,len(cipher))
# dec_txt = lfsr_dec(key,cipher)
# print('\nThe message: ',''.join(dec_txt))
# print(cipher)


# testseed = [1,1,0,0,1,0,1,0,1,1]
# s = bits_to_bit('110101001110010100010101101100100001100111011110\
# 010111010111011011010000001111001001101000110111\
# 00100100100000000110000101101111100011010000')
# testkey = prg_lfsr(feedbackfunc,testseed,len(s))
# testdec_txt = lfsr_dec(testkey,s)
# print('\nTest message: ',''.join(testdec_txt))
#
# print(''.join(txt_dec(bit_to_bits(s))))

