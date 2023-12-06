f = open("input", 'r')
digits = ["    ", "one","two","three","four","five","six","seven","eight","nine"]
s = 0
for line in f:
    line = line.strip()
    print(line)
    firstdigit = 0
    firstdigitpos = 0
    lastdigit = 0
    lastdigitpos = 0
    for pos, c in enumerate(line):
        if c >= '0' and c <= '9':
            firstdigit = int(c)
            firstdigitpos = pos
            break

    for numdigit, strdigit in enumerate(digits):
        f = line.find(strdigit)
        if f >= 0 and f < firstdigitpos:
            firstdigit = numdigit
            firstdigitpos = f

    for pos, c in enumerate(reversed(line)):
        if c >= '0' and c <= '9':
            lastdigit = int(c)
            lastdigitpos = len(line) - pos - 1
            break
    for numdigit, strdigit in enumerate(digits):
        f = line.rfind(strdigit)
        if f >= 0 and f > lastdigitpos:
            lastdigit = numdigit
            lastdigitpos = f

    l = firstdigit * 10 + lastdigit
    s += l
    print(l)

print(s) 
