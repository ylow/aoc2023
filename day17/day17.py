g = [[int(i) for i in x.strip()] for x in open('input','r')]

DIR = [(0,1),(0,-1),(1,0),(-1,0)]

def inbound(g, i,j):
    return i >= 0 and i < len(g) and j >= 0 and j < len(g[0])

memo = {}
def sssp(g, q):
    pq = q
    while len(q) > 0:
        q2 = []
        for ent in q:
            heat,i,j,direction,count = ent
            k = (i,j,direction, count)
            if k in memo:
                if heat >= memo[k]:
                    continue
                memo[k] = min(heat, memo[k])
            else:
                memo[k] = heat
            if i == len(g) - 1 and j == len(g[0]) - 1:
                print(heat, k)
            for d in DIR:
                if count == 3 and d == direction:
                    continue
                if d[0] == -direction[0] and d[1] == -direction[1]:
                    continue
                iinc, jinc = d
                if inbound(g, i+ iinc, j+ jinc):
                    if d == direction:
                        cnt = count + 1
                    else:
                        cnt = 1
                    q2.append((heat + g[i+iinc][j+jinc],i+iinc,j+jinc,d, cnt))
        q = sorted(list(set(q2)))

sssp(g, [(0,0,0,(0,0),0)])

lasti = len(g) - 1
lastj = len(g[0]) - 1
lowestheat = 10000000000
for d in DIR:
    for count in range(4):
        k = (lasti,lastj,d, count)
        if k in memo:
            if lowestheat > memo[k]:
                lowestheat = memo[k]
print(lowestheat) 

