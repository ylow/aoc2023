from inputs4a import *

ret = 0
instances = [1] * len(inputs)
inssize = [0] * len(inputs)
for n, row in enumerate(inputs):
    s = set(row[0])
    c = set(row[1])
    ns = len(s.intersection(c))
    inssize[n] = ns

for n in range(len(inputs)):
    if inssize[n] > 0:
        for j in range(n+1, n+inssize[n]+1):
            if j < len(inputs):
                instances[j] += instances[n]
print(instances)
print(sum(instances))
