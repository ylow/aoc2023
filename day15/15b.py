import collections
f = open('input', 'r').read().strip()
boxes = [collections.OrderedDict() for _ in range(256)]


def hhash(t):
    s = 0
    for c in t:
        s += ord(c)
        s *= 17
        s = s % 256
    return s


s = 0
for e in f.split(','):
    if e[-1] == '-':
        ent = e[:-1]
        boxid = hhash(ent)
        if ent in boxes[boxid]:
            del boxes[boxid][ent]
    else:
        ent,v = e.split('=')
        boxid = hhash(ent)
        boxes[boxid][ent] = int(v)

print(boxes)

s = 0
for i in range(256):
    slot = 1
    for k,v in boxes[i].items():
        s += (i+1) * slot * v
        slot += 1
print(s)


