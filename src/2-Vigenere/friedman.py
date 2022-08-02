import sys
sys.path.append('.')
from support import *

'''
IC AND FRIEDMAN
'''
def ic_en(team):
    ic = 0
    for letter in team:
        ic += team[letter][1] ** 2 # At position team[letter][1] locates the frequency of each letter
    return ic

def ic(team:dict,k:int):
    ic = 0
    for letter in team:
        ml =  team[letter][0]
        ic += (ml*(ml-1))/(k*(k-1))
    return ic


def letter_counter(text)->dict:
    counter = dict.fromkeys(abc,0)
    for letter in text:
        try:
            counter[letter] = counter[letter] +  1
        except KeyError:
            print(letter)
            # counter['-'] = 1
    return dict(sorted(counter.items(), key= lambda x:x[1],reverse=True))

def modulo_back(x:str, y:str):
    d_x = digitalizer(x)[0]
    d_y = digitalizer(y)[0]
    to_char = lambda x: characterizer([x])[0]
    return to_char((d_x - d_y)%abc_len)

def letter_frequency(cipher:str)->dict:
    abc = abc_freq()
    letter_count = letter_counter(cipher)
    for letter, alfabet in zip(letter_count, abc):
        l_times = letter_count[letter]
        guess = characterizer(
            [digitalizer(letter)[0] - digitalizer(alfabet)[0]])[0]
        frequency = l_times/len(cipher)
        letter_count[letter] = (l_times, frequency, alfabet, guess)
    return letter_count



def teams_distinguish(text:str, key_length:int)->dict:
    teams = dict((i+1, []) for i in range(key_length))
    c = 1
    for letter in text:
        teams[c].append(letter)
        c = 1 if c+1>key_length else c+1
    return teams

def teams_counter(teams:dict)->dict:
    for t in teams:
        team = letter_frequency(''.join(teams[t]))
        teams[t] = {'freq': team, 'ic':ic(team, len(teams[t]))}
    return teams


def show_teams(teams_fr:dict):
    abc = abc_freq()
    for key in teams_fr:
        print(f'---*{key}*-TEAM---\nIC: {teams_fr[key]["ic"]}')
        freq = teams_fr[key]['freq']
        for letter, l in zip(freq,abc):
            print(f'{letter}: {freq[letter]} -> {l}')
        print('\n\n')


def reveal_pssw(word:str, teams_freq:dict, key_length:int):
    dec = ['' for i in range(key_length)]
    for team,letter in enumerate(word):
        try:
            dec[team] = teams_freq[team+1]['freq'][letter][3]
        except KeyError:
            dec[team] = '-'
    return ''.join(dec)


def dec_teams(cipher:str,teams_freq:dict, key_length:int):
    c = 0
    for i in range(100):
        word = cipher[i*key_length:(i+1)*key_length]
        pssw = reveal_pssw(word, teams_freq, key_length)
        print(f'{word} -> {pssw}')
        # c = 1 if c+1>key_length else c+1


def teams_creator(text:str, key_length:int, show:bool=False):
    teams = teams_distinguish(text, key_length)
    # print(teams)
    teams_freq = teams_counter(teams)
    if show:
        show_teams(teams_freq)
    return teams_freq


def test_friedman(text:str, in_range):
    key_len = 3
    while key_len<20:
        print(f'Key_Length: {key_len} => ', end='')
        teams = teams_creator(text,key_len)
        max = 0
        for t in teams:
            ic = teams[t]["ic"]
            max = ic if ic > max else max
            print(f'{t}:{ic}', end=', ')
            if  in_range(ic):
                return key_len
        key_len+=1
        print(f'---MAX: {max}---')

def show_teams(teams:dict):
    for i,team in enumerate(teams):
        print(f'---{i+1}---')
        for t in teams[team]['freq']:
            print(f'{t}: {teams[team]["freq"][t]}')
        print('\n\n')

def testing():
    test = 'υφθνγβικψφετθυοζζδητιεοωτετθυοετρηεφβωζκξχβχεμεχτθθσωαχβελγθιερμηητεοωτ'.upper()
    key_len = 5
    teams = teams_creator(test, key_len)
    show_teams(teams)
    # dec_teams(test, teams, key_len)
    # in_range = lambda x: x>=0.0665 and x<=0.0667
    # test_friedman(test,in_range)

def F_test():
    in_range = lambda x: x>=0.0665 and x<=0.0667
    test_friedman(cipher_2,in_range)

#REAVEL PASSWORD
def main():
    key_len = 7
    teams = teams_creator(cipher_2,key_len)
    show_teams(teams)

main()
# testing()
