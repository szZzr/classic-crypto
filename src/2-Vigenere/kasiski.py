import sys
sys.path.append('.')
from support import *

'''
KASISKI
'''
def repeat(word:str, index:int, text:str)->list:
    start = index+len(word)
    indices = [index]
    if word in text[start:]:
        rep = text[start:].index(word)
        indices.append(start+rep)
        start += rep+len(word)
    return indices

def text_traverse(text:str, key_length:int)->dict:
    results = {}
    for i in range(len(text)-key_length+1):
        word = text[i:key_length+i]
        result = repeat(word, i, text)
        if len(result)>1:
            if word in results:
                    results[word] = list(set(results[word]+result))
            else:
                results[word] = result
    return results


def repeats_finder(cipher:str, length:int, repeats:int)->dict:
    findings = {}
    results = text_traverse(cipher, length)
    for word in results.keys():
        if len(results[word]) >= repeats:
            results[word].sort()
            findings.update({word: results[word]})
    return findings

def dist_estimator(the_list):
    return [the_list[i+1]-the_list[i] for i in range(len(the_list)-1)] + [the_list[0]]

def gcd(x, y):
    while (y):
        x, y = y, x % y
    return x

def gcd_list_traverse(llist):
    gcds = []
    for ii,i in enumerate(llist):
        for j in llist[ii+1:]:
            gcds.append(gcd(i,j))
            print(f'{i} _ {j} ==> {gcds[-1]}', end=',\n')
    return gcds

def gcd_finder(repeats:list):
   # llist = list(repeats.values())[0]
   distances = dist_estimator(repeats)
   print(distances, end=':\n')
   print('\n',gcd_list_traverse(distances))


'''
RUNNING MODE
'''
def testing_mode():
    cipher = 'υφθνγβικψφετθυοζζδητιεοωτετθυοετρηεφβωζκξχβχεμεχτθθσωαχβελγθιερμηητεοωτ'
    repeats = repeats_finder(cipher, 3, 2)
    gcd_finder(repeats['ετθ'])


def run(cipher:str, length:int, rep:int, text:str):
    repeats = repeats_finder(cipher, length, rep)
    print(repeats)
    gcd_finder(repeats[text])



# testing_mode()

def main():
    run(cipher_2,4,6,'GZPN')
    run(cipher_2, 5,4, 'GZLRR')
    run(cipher_2, 9,3, 'GVVFRTUNH')

main()
