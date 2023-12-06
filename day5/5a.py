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


ret = []
for s in seeds:
    for m in maps:
        s = applymap(m, s)
    ret.append(s)
print(ret)
print(min(ret))

