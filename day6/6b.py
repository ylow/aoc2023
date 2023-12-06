t = 48876981
d = 255128811171623

r = 0
for n in range(t+1):
    # hold for n seconds so speed is n with remaining time t-n
    distance_travelled = (t-n) * n
    if distance_travelled > d:
        r += 1
print(r)
