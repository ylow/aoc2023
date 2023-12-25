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
   pos.append(p[:2])
   velocity.append(v[:2])

#print(pos)
#print(velocity)

if testing:
    lowlimit = 7
    highlimit = 27
else:
    lowlimit = 200000000000000
    highlimit = 400000000000000

ctr = 0
from fractions import Fraction

for i in range(len(pos)):
    for j in range(i+1, len(pos)):
        pi = pos[i]
        pj = pos[j]
        vi = velocity[i]
        vj = velocity[j]

        # solve for a and b where
        # pi + ta vi = pj + tb vj
        #
        # tb vj - ta vi = pi - pj 
        #
        # check in either coordinate x and y and if they are the same
        # since we are looking for exact intersection we need 
        # deal in the rationals
        V = np.column_stack([vj,-vi])
        P = pi - pj
        
        try:
            r = np.linalg.solve(V, P)
        except:
            continue 
        tb = r[0]
        ta = r[1]
        if tb >= 0 and ta >= 0:
            # intersects
            print(ta, tb)
            ipos = pi + ta * vi
            jpos = pj + tb * vj
            #print(ipos, jpos)
            if ipos[0] >= lowlimit and ipos[0] <= highlimit and \
                    ipos[1] >= lowlimit and ipos[1] <= highlimit:
                print(i,j)
                ctr += 1

print(ctr)
