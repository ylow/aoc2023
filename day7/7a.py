f = open("input", 'r')
s = 0
arr = []

strength = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
def card_to_strength(c):
    # higher strength is stronger
    return [len(strength) - strength.index(i) for i in c]

for line in f:
    line = line.strip()
    card,bid = line.split(' ')
    arr.append((card_to_strength(card),int(bid)))

def cardkey(c):
    # count the occurances
    d = {}
    for i in c:
        if i not in d:
            d[i] = 0
        d[i] += 1

    # 5 of a kind
    if 5 in d.values():
        rt = 100
    elif 4 in d.values():
        rt = 99
    elif 3 in d.values() and 2 in d.values():
        rt = 98
    elif 3 in d.values():
        rt = 97
    elif 2 in d.values() and len(d) == 3:
        # two pair
        rt = 96
    elif 2 in d.values():
        # one pair
        rt = 95
    elif 1 in d.values():
        rt = 94
    return [rt] + c

arr = sorted(arr,key=lambda x: cardkey(x[0]))
s = 0
for i,(_,v) in enumerate(arr):
    s+=(i+1)*v
print(s)
