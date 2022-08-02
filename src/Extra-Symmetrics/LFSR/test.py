# def t(loops,k,realseed):
#     # realseed = [1,1,0,0,1,0,1,0,1,1]
#     # k = [0, 0, 1, 1, 0, 1, 1, 1, 0, 1]
#     s= []
#     key = []
#     for i in range(loops):
#         print(k)
#         s.append(k[9]^k[7]^k[6]^k[0])
#         # print("k9:" +str(k[9])+"\tk8: " +str(k[8])+"\tk6: " +str(k[6])+"\tk0: " +str(k[0])+"\n")
#         k = k[1:10]
#         k.append(s[i])
#         key.append(k[9])
#         if(k == realseed):
#             print('The real seed: ' + str(i))
#     i=0
#     while(k!=realseed):
#         # print(k)
#         s.append(k[9]^k[7]^k[6]^k[0])
#         k = k[1:10]
#         k.append(s[i])
#         i+=1
#     # print(i)
#     print(key)


# real_seed = [1,1,0,0,1,0,1,0,1,1]
# k = [1,0,0,1,0,1,0,0,0,1]
# ffunc = [0,0,0,0,0,1,1,0,1,1]

#
# s = []
# s.append(k[9]^k[8]^k[6]^k[0])
# k = k[1:10]
# print(k)
# k.append(s[0])
# print(k)
#
# t(30,k,real_seed)

# def seedFinder(keystream,bits,ffunc):
#     index=[]
#     for i in range(len(ffunc)):
#         if ffunc[i]==1:
#             index.append(i)
#     rev_kstream = keystream[::-1]
#     for i in range(bits):
#         f = rev_kstream[index[0]]
#         for k in range(1,len(index)):
#             f^=rev_kstream[index[k]]
#          # f = rev_kstream[0]^rev_kstream[6]^rev_kstream[7]^rev_kstream[9]
#         rev_kstream = rev_kstream[1:len(rev_kstream)]
#         rev_kstream.append(f)
#     print(str(rev_kstream))


def seed_finder(keystream):
    r_keystream = keystream[::-1] #reverse keystream
    for i in range(len(keystream)):
        f = r_keystream[0]^r_keystream[6]^r_keystream[7]^r_keystream[9] #feedback function for previous
        r_keystream = r_keystream[1:10]
        r_keystream.append(f)
    print(str(r_keystream))


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

def PRG(seed,ffunc,msg_bits):
    lfsr = []
    c = fb_table_creator(ffunc)
    for i in range(msg_bits):
        lfsr.append(seed[len(seed)-1])
        seed = array_multiplier(c,seed)
    return lfsr


real_seed = [1,1,0,0,1,0,1,0,1,1]
k = [1,0,0,1,0,1,0,0,0,1]
ffunc = [0,0,0,0,0,1,1,0,1,1]

c = fb_table_creator(k)
x1 = array_multiplier(c,real_seed)
print(x1)
x2 = array_multiplier(c,x1)
print (x2[len(x2)-1])
