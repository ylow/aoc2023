from collections import defaultdict
graph = defaultdict(lambda : [])
for l in open("input2","r"):
    l, r = l.strip().split(':')
    l = l.strip()
    r = [x.strip() for x in r.strip().split(' ')]
    for j in r:
        graph[l].append(j)
        graph[j].append(l)

print ("graph g{")
for k,v in graph.items():
    for j in v:
        if k< j:
            print(f"{k} -- {j}")
print("}")
# from plotting graph with neato, these 3 are the edges
# kzh -- rks
# ddc -- gqm
# tnz -- dgt
print(len(graph), "vertices")

visited = defaultdict(lambda : False)
q = [list(graph.keys())[0]]
while len(q) > 0:
    q2 = []
    for v in q:
        if visited[v] == True:
            continue
        for nbr in graph[v]:
            q2.append(nbr)
        visited[v] = True
    q = list(set(q2))

print(len(visited))
print(len(visited) * (len(graph) - len(visited)))
