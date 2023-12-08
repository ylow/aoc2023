f = open("input", 'r')
instructions = f.readline().strip()
f.readline()

def wrangle(l):
    (n,lr) = [x.strip() for x in l.split('=')]
    (left, right) = [x.strip() for x in lr[1:-1].split(',')]
    return (n, (left, right))

lines = [wrangle(x.strip()) for x in f.readlines()]
graph = {l[0]:l[1] for l in lines}

def find_cycle(c):
    curn = c
    insc = 0
    cyc = []
    while (insc % len(instructions), curn) not in cyc:
        cyc.append((insc % len(instructions), curn))
        i = instructions[insc % len(instructions)]
        i = ['L','R'].index(i)
        curn = graph[curn][i]
        insc += 1

    return (cyc, cyc.index((insc % len(instructions), curn)))

starts = [x for x in graph if x[-1] == 'A']

Cmod= []
Cr = []
Cyclestart = []
for i in starts:
    cycle, cyclepos = find_cycle(i)
    zc = []
    for z, n in enumerate(cycle):
        if n[1][-1] == 'Z':
            zc.append(z)
    assert(len(zc) == 1)
    Cr.append(zc[0])
    Cmod.append(len(cycle) - cyclepos)
    Cyclestart.append(cyclepos)
    print (zc, cyclepos)
    print(Cr)
    print(Cmod)
    print(Cyclestart)

# Very conveniently the cycle length is *exactly* the location of Z
for i in range(len(Cmod)):
    assert(Cmod[i] == Cr[i])

# so I only need to solve a series of 
# K == 0 mod Cmod1
# K == 0 mod Cmod2
# K == 0 mod Cmod3
# ...

# So this is just the prime factorization of all the Cmods multiplied together

def primefact(p):
    assert(p>1)
    pfact = {}
    while p > 1:
        for i in range(2, p+1):
            if p % i == 0:
                p = p // i
                if i in pfact:
                    pfact[i] += 1
                else:
                    pfact[i] = 1
                break
    return pfact

pfact = {}
for i in Cmod:
    pf = primefact(i)
    for k,v in pf.items():
        if k not in pfact:
            pfact[k] = v
        else:
            pfact[k] = max(v,pfact[k])

print(pfact)

res = 1
for k,v in pfact.items():
    for z in range(v):
        res = res * k
print(res)

