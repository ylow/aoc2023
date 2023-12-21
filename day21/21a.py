m = [list(x.strip()) for x in open('input','r')]

for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == 'S':
            start = (i,j)
            m[i][j] = '.'

def inbound(i,j):
    if i >= 0 and j >=0 and i < len(m) and j < len(m[0]):
        if m[i][j] == '.':
            return True
    return False
q = [start]
for i in range(64):
    q2 = []
    for i,j in q:
        if inbound(i-1,j):
            q2.append((i-1,j))
        if inbound(i+1,j):
            q2.append((i+1,j))
        if inbound(i,j-1):
            q2.append((i,j-1))
        if inbound(i,j+1):
            q2.append((i,j+1))
    q = list(set(q2))

print(len(q))
