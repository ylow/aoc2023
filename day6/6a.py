instances = [[48,255], [87,1288],[69,1117],[81,1623]]

tr = []
for (t,d) in instances:
    r = 0
    for n in range(t+1):
        # hold for n seconds so speed is n with remaining time t-n
        distance_travelled = (t-n) * n
        if distance_travelled > d:
            r += 1
    tr.append(r)
print(tr)
print(tr[0] * tr[1] * tr[2] * tr[3])
