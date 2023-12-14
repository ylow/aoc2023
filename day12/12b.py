f = [x.strip() for x in open("input", "r")]

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

def search(s, cons, idx, memo):
    if idx == len(s):
        return sprcount(s) == cons
    if idx > 0 and s[idx-1] != '#':
        partialcons = sprcount(s[:idx-1])
        if partialcons != cons[:len(partialcons)]:
            return 0
        partialcons = tuple(partialcons)
        if (idx, partialcons) in memo:
            return memo[(idx, partialcons)]

    if s[idx] == '?':
        a = 0
        s[idx] = '.'
        if idx > 0 and s[idx-1] == '.':
            a += search(s, cons, idx + 1, memo)
        else:
            # an impossibility filter
            partialcons2 = sprcount(s[:idx])
            if cons[:len(partialcons2)] == partialcons2:
                a += search(s, cons, idx + 1, memo)
        s[idx] = '#'
        a += search(s, cons, idx + 1, memo)
        s[idx] = '?'
        if idx > 0 and s[idx-1] != '#':
            memo[(idx, partialcons)] = a
        return a
    else:
        return search(s, cons, idx + 1, memo)


total = 0
maxways = 0
maxs = ""
for l in f:
    s , cons = l.split(' ')
    ts = l 
    s = list(s)
    cons = [int(i) for i in cons.split(',')]
    s = s + ['?'] + s + ['?'] + s + ['?'] + s + ['?'] + s
    cons = cons * 5
    ways = search(s, cons, 0, {})
    if ways > maxways:
        maxways = ways
        maxs = ts
    print(ways)
    total += ways

print(total)
print(maxways)
print(maxs)
