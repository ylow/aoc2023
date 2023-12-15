f = open('input', 'rb').read()
s = 0
t = 0
for c in f:
    if c == ord('\n'):
        continue
    if c == ord(','):
        t += s
        s = 0
        continue
    s += c
    s *= 17
    s = s % 256
t += s

print(s)
print(t)
