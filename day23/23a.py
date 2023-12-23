m = [list(x.strip()) for x in open('input','r')]

q = [(0,1)]
end = (len(m) - 1, len(m[0]) - 2)
visited = [[0] * len(m[0]) for _ in range(len(m))]

def inbound(i, j):
    return i >= 0 and j >=0 and i < len(m) and j < len(m[0]) and m[i][j] != '#'

def search(i,j, length):
    if (i,j) == end:
        return length
    if visited[i][j]:
        return 0
    visited[i][j] = True
    bestpath = 0
    if m[i][j] == '>':
        bestpath = max(bestpath, search(i,j+1, length+1))
    elif m[i][j] == '<':
        bestpath = max(bestpath, search(i,j-1, length+1))
    elif m[i][j] == 'v':
        bestpath = max(bestpath, search(i+1,j, length+1))
    elif m[i][j] == '^':
        bestpath = max(bestpath, search(i-1,j, length+1))
    else:
        if inbound(i-1,j):
            bestpath = max(bestpath, search(i-1,j, length+1))
        if inbound(i+1,j):
            bestpath = max(bestpath, search(i+1,j, length+1))
        if inbound(i,j-1):
            bestpath = max(bestpath, search(i,j-1, length+1))
        if inbound(i,j+1):
            bestpath = max(bestpath, search(i,j+1, length+1))
    visited[i][j] = False
    return bestpath
import sys
sys.setrecursionlimit(100000)
print(search(0,1,0))
