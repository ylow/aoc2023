f = [list(s.strip()) for s in open('input', 'r')]

height = len(f)
width = len(f[0])

vertweights = [1] * height
horzweights = [1] * width
extrai = []
extraj = []
for i in range(height):
    if all(x == '.' for x in f[i]):
        vertweights[i] = 1000000

for j in range(width):
    if all(f[i][j] == '.' for i in range(height)):
        horzweights[j] = 1000000


galaxies = []
for i in range(height):
    for j in range(width):
        if f[i][j] == '#':
            galaxies.append((i,j))

print(f"{galaxies} Galaxies")
print(f"{vertweights}")

def mdist(a,b):
    istart = min(a[0], b[0])
    iend = max(a[0], b[0])
    jstart = min(b[1], a[1])
    jend = max(b[1], a[1])
    return sum(vertweights[istart+1:iend+1]) + sum(horzweights[jstart+1:jend+1]) 

tdist = 0
for g1 in range(len(galaxies)):
    for g2 in range(g1, len(galaxies)):
        tdist += mdist(galaxies[g1], galaxies[g2])

print(tdist)
