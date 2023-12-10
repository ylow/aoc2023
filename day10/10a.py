f = open("input", 'r')
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

bestval = 0 
bestloc = (0,0)
for i, l in enumerate(p):
    for j, x in enumerate(l):
        if x > bestval and x < initval:
            bestval = x
            bestloc = (i,j)

print(bestval)
print(bestloc)
