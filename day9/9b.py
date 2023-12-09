def extra(v):
    assert(len(v) > 0)
    if all([x == v[0] for x in v]):
        return v[0]
    t=[]
    for i in range(len(v) - 1):
        t.append(v[i+1] - v[i])
    return v[0] - extra(t)

f = open("input", 'r')
ext = []
for line in f:
    vals = [int(x) for x in line.split(' ')]
    ext.append(extra(vals))

print(ext)
print(sum(ext))
