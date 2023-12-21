m = [list(x.strip()) for x in open('input','r')]
emptycells = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == 'S':
            start = (i,j)
            m[i][j] = '.'
        emptycells += m[i][j] == '.'
print(emptycells)
cycle = [7424, 7436]
def inbound(i,j):
    return m[i % len(m)][j % len(m[0])] == '.'

def switchboard(i,j):
    si = 0
    sj = 0
    if i >= len(m):
        si = 1
    elif i < 0:
        si = -1
    if j >= len(m[0]):
        sj = 1
    elif j < 0:
        sj = -1
    return (si, sj)

steps = [(1, 0), (-1,0),(0,-1),(0,1)]
q = {(start[0], start[1]): set([(0, 0)])}
fullboards = set(())

central_board_cycle_start = 128
other_cycle_time = 131

boards_in_cycle_pos = [0,0]
s = 0
it = 0
while it + 131< 26501365:
    it += 131
    s += 1
    if s == 1:
        boundary = 1
    else:
        boundary = 4 + (s-2) * 4
    boards_in_cycle_pos = [boards_in_cycle_pos[1], boards_in_cycle_pos[0] + boundary]

print(boards_in_cycle_pos)
# 65 swaps the cycle around
print(boards_in_cycle_pos[0] * cycle[1] + boards_in_cycle_pos[1] * cycle[0])
print(26501365 - it, "iterations Remaining")
print(s+1, "Boundary size")
for it in range(1, 1000):
    q2 = {}
    for v, c in q.items():
        (i,j) = v
        for s in steps:
            ni, nj = i + s[0], j + s[1]
            if not inbound(ni, nj):
                continue
            bi, bj = switchboard(ni, nj)
            ni = ni % len(m)
            nj = nj % len(m[0])
            rs = set() 
            for boardsi, boardsj in c:
                if (boardsi + bi, boardsj + bj) in fullboards:
                    continue
                rs.add((boardsi + bi, boardsj + bj))
            if (ni, nj) not in q2:
                q2[(ni, nj)] = rs
            else:
                rs = rs.union(q2[(ni, nj)])
                q2[(ni, nj)] = rs
    bcount = {}
    newfboards = set(())
    tsum = 0
    for k, v in q2.items():
        tsum += len(v)
        for b in v:
            if b not in bcount:
                bcount[b] = 0
            bcount[b] += 1
    print(it, it % 131, bcount)
    if it % 131 == 65:
        print("-------------------")
        print(it//131, "==>" ,tsum)
#    for k, v in bcount.items():
#        if v == cycle[0]:
#            fullboards.add(k)
#            newfboards.add(k)
#            print(f"{it} Fullboard {k}")
    for k in q2:
        q2[k] = q2[k].difference(newfboards)
    q = q2

s = 0
for k, v in q.items():
    s += len(v)
print(s)
