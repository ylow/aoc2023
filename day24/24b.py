import numpy as np
testing = False
fname = "input"
if testing:
    fname = "testinput"
lines = [x.strip() for x in open(fname,"r")]

pos = []
velocity = []
for l in lines:
   p, v = [np.array([float(i.strip()) for i in x.strip().split(',')], 'd') for x in l.split('@')]
   pos.append(p)
   velocity.append(v)

# 3 equations suffice
pos = pos[:3]
velocity = velocity[:3]

#print(pos)
#print(velocity)

if testing:
    lowlimit = 7
    highlimit = 27
else:
    lowlimit = 200000000000000
    highlimit = 400000000000000

from sympy import solve, Symbol, symbols
from sympy.matrices import Matrix

a1,a2,a3 = symbols("a1,a2,a3")
w1,w2,w3 = symbols("w1,w2,w3")
t1,t2,t3 = symbols("t1,t2,t3")

ts = [t1,t2,t3]
aas = [a1,a2,a3]
ws = [w1,w2,w3]
eqs = []
for i in range(len(pos)):
    for j in range(3):
        p = pos[i][j]
        v = velocity[i][j]
        lhs = p + ts[i] * v
        rhs = aas[j] + ts[i] * ws[j]
        eqs.append(lhs - rhs)

s = solve(eqs, [a1,a2,a3,w1,w2,w3,t1,t2,t3], dict=True)
print(s)
s = s[0]
print(s[a1] + s[a2] + s[a3])
