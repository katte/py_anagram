import itertools
words = []
with open('words.italian.txt') as f:
    words = f.read().split('\n')

def charCount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict

def possible_words(lwords, charSet):
    l = []
    for word in lwords:
        flag = 1
        chars = charCount(word)
        for key in chars:
            if key not in charSet:
                flag = 0
            else:
                if charSet.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            l.append(word)
    return l


def check(s1, s2):
    if len(s1) != len(s2):
        return False
    if (sorted(s1) == sorted(s2)):
        return True
    return False

if __name__ == "__main__":
    word = input('Inserisci parola da anagrammare: ').lower().strip()
    print('')
    word = ''.join([i for i in word if i.isalpha()])
    minwordlen = int(input('Inserisci la lunghezza minima delle parole: '))
    print('')
    charSet = [char for char in word]
    pw = possible_words(words, charSet)

    pw = [x for x in pw if len(x)>=minwordlen]
    print(f'List of all possible words made from: {word}')
    print(pw)
    print('Ok, check if there are some anagrams...')
    for i in range(2, 10):
        for l in itertools.permutations(pw, r=i):
            aw = ''.join(l)
            # print(f'Check: {aw}')
            x = check(word, aw)
            if x:
                print(l)









