f = open("input", 'r')
instructions = f.readline().strip()
f.readline()

def wrangle(l):
    (n,lr) = [x.strip() for x in l.split('=')]
    (left, right) = [x.strip() for x in lr[1:-1].split(',')]
    return (n, (left, right))

lines = [wrangle(x.strip()) for x in f.readlines()]
graph = {l[0]:l[1] for l in lines}


curn = 'AAA'
insc = 0
while curn != 'ZZZ':
    i = instructions[insc % len(instructions)]
    i = ['L','R'].index(i)
    curn = graph[curn][i]
    insc += 1

print(insc)
