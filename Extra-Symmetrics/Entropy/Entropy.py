alphabet = {'Α': 11.58, 'Β': 0.55, 'Γ': 1.72, 'Δ': 1.64, 'Ε': 8.23, 'Ζ': 0.27, 'Η': 5.01, 'Θ': 1.11,
            'Ι': 9.53, 'Κ': 4.18, 'Λ': 2.78, 'Μ': 3.51, 'Ν': 6.18, 'Ξ': 0.35, 'Ο': 10.15, 'Π': 4.01,
            'Ρ': 4.03, 'Σ': 7.63, 'Τ': 7.71, 'Υ': 4.22, 'Φ': 0.88, 'Χ': 0.46, 'Ψ': 0.16, 'Ω': 2.11}

abc_el = {'ά': 'α', 'έ': 'ε', 'ή': 'η', 'ί': 'ι', 'ΰ': 'υ', 'α': 'α', 'β': 'β', 'γ': 'γ', 'δ': 'δ', 'ε': 'ε', 'ζ': 'ζ',
          'η': 'η', 'θ': 'θ', 'ι': 'ι', 'κ': 'κ', 'λ': 'λ', 'μ': 'μ', 'ν': 'ν', 'ξ': 'ξ', 'ο': 'ο', 'π': 'π', 'ρ': 'ρ',
          'ς': 'σ', 'σ': 'σ', 'τ': 'τ', 'υ': 'υ', 'φ': 'φ', 'χ': 'χ', 'ψ': 'ψ', 'ω': 'ω', 'ϊ': 'ι', 'ϋ': 'υ', 'ό': 'ο',
          'ύ': 'υ', 'ώ': 'ω'}


def textedit(path,abc_el):
    import codecs
    f=[]
    with codecs.open(path, 'r', 'mac_greek') as file:
            f = list(file.read())
    a = 0
    for i in range(len(f)):
        if f[i] == ' ' or f[i] == '\n' or ord(f[i]) < 902 or ord(f[i]) > 975:
            a += 1
    a = len(f) - a
    for i in range(a):
        if f[i] == ' ' or f[i] == '\n' or ord(f[i]) < 902 or ord(f[i]) > 975:
            f.pop(i)
    for i in range(len(f)):
        if ord(f[i])>=940 and ord(f[i])<=974:
            f[i] = abc_el.get(f[i])
        f[i] = f[i].upper()
    with codecs.open(path,'w','mac_greek') as file:
        file.writelines(f)
    return f


def greek_randomchar_entropy():
    import math
    h = 0
    for i in range(24):
        h += -(1 / 24) * math.log(1 / 24, 2)
    return round(h, 4)


def greek_alphabet_entropy(alphabet):
    '''
    calculate 1st class entropy
    :param alphabet: dictionary of text's alphabet frequency
    :return: 1st class entropy
    '''
    import math
    h = 0
    ab = [chr(i+913) for i in range(25)]
    ab.pop(17)
    for i in range(len(ab)):
        p = alphabet.get(ab[i]) / 100
        h += -p * math.log(p, 2)
    return round(h, 4)


def greek_alphabet_2entropy(alphabet,double_alphabet):
    '''
    calculate 2nd class entropy
    :param alphabet: dictionary of text's alphabet frequency
    :param double_alphabet: dictionary of text's double char alphabet frequency
    :return: 2nd class entropy
    '''
    import math
    doubleab = [] # list with split keys
    for doublechar in double_alphabet:
        doubleab.append(list(doublechar))
    h1=0
    h2=0
    for d in doubleab:
        if d[0] in alphabet:
            # p = alphabet.get(d[0]) / 100
            p_double = double_alphabet.get(''.join(d[0]+d[1])) / 100
            # h1 += p * math.log(p, 2)
            h2 += p_double * math.log(p_double, 2)
    h1 = greek_alphabet_entropy(alphabet)
    h = 0.5*(h1 - h2)
    return h

def greek_char_frequency(data):
    '''
    calculate the frequency of greek text's chars
    :param data: list with the text
    :return: dictionary with greek chars frequency of data
    '''
    ab = [chr(i+913) for i in range(25)]
    ab.pop(17)
    alphabet= {ab[i]:0 for i in range(24)}
    for i in range(len(data)):
        if data[i] in alphabet:
            alphabet[data[i]] += 1
    lendata = len(data)
    for key in alphabet:
        alphabet[key] =  round(100*(alphabet[key] / lendata),2)
    return alphabet


def greek_doublechar_frequency(data):
    ldata = len(data)
    alphabet = {}
    for i in range(1,ldata):
        s = data[i-1]+data[i]
        if s in alphabet:
            alphabet[s]+=1
        else:
            alphabet[s]=1
    abkeys = list(alphabet.keys())
    print(len(abkeys))
    for i in range(len(abkeys)): #frequency of chars
        alphabet[abkeys[i]] = round(alphabet[abkeys[i]]/ldata*100,2)
    return alphabet

# random greek char entropy
f0 = greek_randomchar_entropy()
f1 = greek_alphabet_entropy(alphabet)
r = 1 - f1/f0
print('Random greek char\n')
print('Random greek char entropy: ', f0)
print('Greek alphabet entropy: ', f1)
print('Redundancy random-char: ', round(r,3),'(',100*round(r,3),'%)')


# 1st class entropy
mydata = textedit('greektxt.txt',abc_el)
myalphabet = greek_char_frequency(mydata)
myf1 = greek_alphabet_entropy(myalphabet)
myr1 = 1 - myf1/f0
print('\n\n1st class entropy\n')
print(myalphabet)
print('Entropy of greek language 1stApproach: ',myf1)
print('Redundancy 1st: ', round(myr1,2),'(',100*round(myr1,4),'%)')



#2nd class entropy
my2alphabet = greek_doublechar_frequency(mydata)
myf2 = greek_alphabet_2entropy(myalphabet,my2alphabet)
myr2 = 1 - myf2/f0
print('\n\n2nd class entropy (double-char)\n')
print(my2alphabet)
print('Entropy of greek language 2ndApproach: ',myf2)
print('Redundancy 2nd: ', round(myr2,4),'(',100*round(myr2,4),'%)')
