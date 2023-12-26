import numpy as np
import scipy
nodes = {}
deg = {}
elist = []
for line in open("size-1048576.txt","r"):
    lhs, r = line.strip().split(':')
    i = lhs.strip()
    r = [x.strip() for x in r.strip().split(' ')]
    for j in r:
        if i not in nodes:
            nodes[i] = len(nodes)
        if j not in nodes:
            nodes[j] = len(nodes)
        ni = nodes[i]
        nj = nodes[j]
        if ni not in deg:
            deg[ni] = 0
        if nj not in deg:
            deg[nj] = 0
        deg[ni] += 1
        deg[nj] += 1
        elist.append((ni,nj, 1))
        elist.append((nj,ni, 1))

elist = np.array(elist)
print(elist)
lap = scipy.sparse.coo_array((elist[:,2], (elist[:,0], elist[:,1]))).asfptype()
val, vecs = scipy.sparse.linalg.eigs(lap, k = 2)
vecs = np.real(vecs)
import sklearn.cluster
model = sklearn.cluster.KMeans(2)
model.fit(vecs)

# labels are 0 or 1. So summing it will give us the size of one cluster
clustersize = model.labels_.sum() 
print(clustersize * (len(nodes) - clustersize))

