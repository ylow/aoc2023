from inputs4a import *

ret = 0
for row in inputs:
    s = set(row[0])
    c = set(row[1])
    inssize = len(s.intersection(c))
    if inssize > 0:
        score = 2**(inssize - 1)
        print(s,c,s.intersection(c), score)
        ret += score
print(ret)
