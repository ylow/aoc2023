f = open("input", 'r')
s = 0
for line in f:
    line = line.strip()
    print(line)
    firstdigit = 0
    lastdigit = 0
    for c in line:
        if c >= '0' and c <= '9':
            firstdigit = int(c)
            break

    for c in reversed(line):
        if c >= '0' and c <= '9':
            lastdigit = int(c)
            break
    l = firstdigit * 10 + lastdigit
    s += l
    print(l)

print(s) 
