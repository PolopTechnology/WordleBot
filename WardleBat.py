import numpy as np
from tqdm import tqdm

def yellow(db, txt, yel_pos):
    letter = txt[yel_pos]
    res = [i for i in db if letter in i]
    res = [i for i in res if not letter == i[yel_pos]]
    return res

def green(db, txt, grn_pos):
    letter = txt[grn_pos]
    res = [i for i in db if letter == i[grn_pos]]
    return res

def gray(db, txt, gry_pos):
    letter = txt[gry_pos]
    res = [i for i in db if not letter in i]
    return res

def result(db, txt, results):
    res = db
    for i, x in enumerate(results):
        if x == 0: res = gray(res, txt, i)
        if x == 1: res = yellow(res, txt, i)
        if x == 2: res = green(res, txt, i)
    return res

def values(db):
    final_vals = {}
    for i in tqdm(db):
        val = []
        for j in poss:
            try:
                res = len(result(db, i, j))
                val.append((res + freq[i])/(len(db) + le))
            except:
                pass
        try:
            final_vals[i] = sum(val)/len(val)
        except:
            pass
    final_vals = dict(sorted(final_vals.items(), key=lambda item: item[1]))
    #print(final_vals)
    #print(max(list(final_vals.values())))
    return list(final_vals.keys())[-1]

q = open("WordleWords.txt").read().split()
freq = [i for i in open("freqWord.txt").read().replace(",", " ").split() if i.isalpha()][2:]
freq = [i for i in freq if len(i) == 5]
freq.sort(reverse=True)
freqlen = [i for i, word in enumerate(freq)]
le = len(freq)
freq = dict(zip(freq, freqlen))

print(freq['there'])

poss = []
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                for m in range(3):
                    poss.append([i,j,k,l,m])

#next_word = values(q)
next_word = "abbey"
print(next_word)
db = q
for i in range(5):
    res = [int(i) for i in input().split()]
    #print(db)
    if res == [2, 2, 2, 2, 2]:
        print("HOORAy!")
        break
    db = result(db, next_word, res)
    next_word = values(db)
    print(next_word)