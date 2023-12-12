f = [x.strip() for x in open("testinput", "r")]

def sprcount(l):
    c = []
    ctr = 0
    for i in l:
        if i == '#':
            ctr += 1
        elif ctr > 0:
            c.append(ctr)
            ctr = 0
    if ctr:
        c.append(ctr)
    return c

def search(s, cons, idx):
    if idx == len(s):
        return sprcount(s) == cons
    if s[idx] == '?':
        s[idx] = '#'
        a = search(s, cons, idx + 1)
        s[idx] = '.'
        a += search(s, cons, idx + 1)
        s[idx] = '?'
        return a
    else:
        return search(s, cons, idx + 1)


total = 0
for l in f:
    s , cons = l.split(' ')
    s = list(s)
    cons = [int(i) for i in cons.split(',')]
    ways = search(s, cons, 0)
    print(ways)
    total += ways

print(total)

