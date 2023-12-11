f = open("testinput", 'r')
g = [list(l.strip()) for l in f]
mi = len(g)
mj = len(g[0])
initval = 10000000000
p = [[initval] * mj for i in range(mi)]


start  = None
for i, l in enumerate(g):
    for j, x in enumerate(l):
        if x == 'S':
            start = (i,j)
            break
    if start is not None:
        break

si,sj = start[0], start[1]
p[si][sj] = 0

adj = {}
adj['-'] = [(0,-1), (0,1)]
adj['|'] = [(-1,0), (1,0)]
adj['.'] = []
adj['L'] = [(-1,0), (0,1)]
adj['J'] = [(-1,0), (0,-1)]
adj['7'] = [(1,0), (0,-1)]
adj['F'] = [(1,0), (0,1)]
adj['S'] = []
q = []
q.append(start)

# ok. we actually need to figure out what 'S' is.
firstnbrs = []
for ii in range(si-1,si+2):
    if ii < 0 or ii >= mi:
        continue
    for jj in range(sj-1,sj+2):
        if jj < 0 or jj >= mj:
            continue
        for di, dj in adj[g[ii][jj]]:
            iii,jjj = ii + di , jj + dj
            if iii == si and jjj == sj:
                firstnbrs.append((ii,jj))
                break

firstnbrs = list(set(firstnbrs))
print(firstnbrs)
for k,v in adj.items():
    if len(v) == 0:
        continue
    ok = True
    for di, dj in v:
        ok = ok and (di+si,dj+sj) in firstnbrs 
    if ok:
        g[si][sj] = k
        print(f"starting pos inferred as {k}")

q = [(si, sj)]
while len(q) > 0:
    q2 = []
    for (i,j) in q:
        for di, dj in adj[g[i][j]]:
            ii,jj = i + di, j + dj
            nval = p[i][j] + 1
            if nval < p[ii][jj]:
                q2.append((ii,jj))
                p[ii][jj] = nval
    q = list(set(q2))

# bit field of pipe location
p = [[int(x < initval) for x in l] for l in p]
for i in range(mi):
    for j in range(mj):
        if p[i][j]:
            continue
        else:
            g[i][j] = '.'

verts = "|LJ7F"
ctr = 0
for i in range(mi):
    enclosed = False
    onboundary = None 
    print(p[i])
    print(''.join(g[i]))
    for j in range(mj):
        if p[i][j]:
            if onboundary:
                if g[i][j] == '-':
                    continue
                elif g[i][j] == onboundary:
                    onboundary = None
                    continue
                elif g[i][j] in verts:
                    enclosed = not enclosed
                    onboundary = None 
            elif g[i][j] in verts:
                # Special case L---7 and F---J
                # These two cases boundary cases effectively
                # behave as if it is shifted upwards by a teeny bit.
                if g[i][j] == 'L':
                    onboundary = '7' 
                elif g[i][j] == 'F':
                    onboundary = 'J' 
                enclosed = not enclosed
        if p[i][j] == 0 and g[i][j] == '.' and enclosed:
            ctr += 1
print(ctr)
