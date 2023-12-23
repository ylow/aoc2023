import hashlib
import pickle
cache_hit = 0
m = [list(x.strip()) for x in open('input','r')]

spacecount = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] in '<>^v':
            m[i][j] = '.'
            spacecount += 1

q = [(0,1)]
end = (len(m) - 1, len(m[0]) - 2)
print(end)
visited = [[0] * len(m[0]) for _ in range(len(m))]



def inbound(i, j):
    return i >= 0 and j >=0 and i < len(m) and j < len(m[0]) and m[i][j] != '#'

def is_intersection(i, j):
    if m[i][j] == '.':
        return (m[i-1][j] == '.')  + (m[i+1][j] == '.' ) + (m[i][j-1] == '.') + (m[i][j+1] == '.') >= 3
    return False

intersections = [(0,1),end]
for i in range(1, len(m)-1):
    for j in range(1, len(m[0])-1):
        if is_intersection(i,j):
            intersections.append((i,j))

edges = {}
for i in range(len(intersections)):
    edges[i] = []
print(intersections)
steps = [(-1,0),(1,0),(0,-1),(0,1)]
for idx, ins in enumerate(intersections):
    visited = [[0] * len(m[0]) for _ in range(len(m))]
    print(idx)
    q = [(ins[0], ins[1], 0)]
    while len(q) > 0:
        q2 = []
        for i,j,l in q:
            visited[i][j] = True
            if (i,j) in intersections:
                idx2 = intersections.index((i,j))
                if idx2 != idx:
                    edges[idx].append((idx2, l))
                    edges[idx2].append((idx, l))
                    continue
            for si,sj in steps:
                ti = i + si
                tj = j + sj
                if inbound(ti, tj) and not visited[ti][tj]:
                    q2.append((ti, tj, l+1))
        q = list(set(q2))

for i in range(len(intersections)):
    edges[i] = list(set(edges[i]))
    for e, l in edges[i]:
        if e > i:
            print(f'{i} -- {e} [label="{l}"]')

biggestknown = 0
def search(visited, idx, length):
    global biggestknown
    if idx in visited and visited[idx] == True:
        return 0 
    if idx == 1:
        if length > biggestknown:
            print(biggestknown)
            biggestknown = length
        return length
    visited[idx] = True
    m = 0
    for i,l in edges[idx]:
        m = max(m, search(visited, i, length + l))
    visited[idx] = False
    return m

print(search({}, 0, 0))
