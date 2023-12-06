seeds = [int(i) for i in open("seeds", 'r').read().split(' ')]

def readmaps(fname):
    f = open(fname, 'r')
    ret = []
    for r in f.readlines():
        r = [int(i) for i in r.split(' ')]
        assert(len(r) == 3)
        ret.append(r)
    return ret

maps = []
for i in [1,2,3,4,5,6,7]:
    maps.append(readmaps('m' + str(i)))

def applymap(m,num):
    for (t,s,l) in m:
        if num >= s and num < s + l:
            num = t + (num - s)
            return num
    return num

def applyrmap(m,num):
    for (s,t,l) in m:
        if num >= s and num < s + l:
            num = t + (num - s)
            return num
    return num

seeds2 = [(seeds[2*i], seeds[2*i+1]) for i in range(len(seeds)//2)]
assert(len(seeds2)*2 == len(seeds))

boundaries = []
for m in reversed(maps):
    boundaries.append(0)
    boundaries.append(4000000000)
    for (t,s,l) in m:
        boundaries.append(t)
        boundaries.append(t+l-1)
        boundaries.append(t+l)
    newboundaries = []
    for b in boundaries:
        newboundaries.append(applyrmap(m,b))
    boundaries = newboundaries
print(boundaries)
for (t,s,l) in maps[0]:
    boundaries.append(s)
    boundaries.append(s+l-1)
    boundaries.append(s+l)

boundaries = sorted(boundaries)
minloc = -1
for start,count in seeds2:
    print(start,count)
    candidates = []
    candidates.append(start)
    candidates.append(start + count - 1)
    for b in boundaries:
        if b > start and b < start + count:
            candidates.append(b)

    for s in candidates:
        for m in maps:
            s = applymap(m, s)
        if minloc == -1 or s < minloc:
            minloc = s
print(minloc)

