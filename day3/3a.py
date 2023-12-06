f = open("input", 'r')
sc = []
npos = []
nums = []
sympos = set()
for line in f:
    line = line.strip()
    print(line)
    
    firstdigit = -1
    lastdigit = -1 
    for pos, c in enumerate(line):
        if c >= '0' and c <= '9':
            if firstdigit == -1:
                firstdigit = pos
                lastdigit = pos
            else:
                lastdigit = pos
        else:
            if lastdigit != -1:
                npos.append(((len(sc), firstdigit), (len(sc), lastdigit)))
                nums.append(int(line[firstdigit:lastdigit+1]))
                firstdigit = -1
                lastdigit = -1
            if c != '.':
                sympos.add((len(sc), pos))
    if lastdigit != -1:
        npos.append([(len(sc), firstdigit), (len(sc), lastdigit)])
        nums.append(int(line[firstdigit:]))

    sc.append(line)

totalsum = 0
for num, (startc, endc) in zip(nums, npos):
    # positions are inclusive so +2
    done = False
    for x in range(startc[0] - 1, endc[0] + 2):
        for y in range(startc[1] - 1, endc[1] + 2):
            if (x,y) in sympos:
                totalsum += num
                done = True
                break
        if done:
            break
print(totalsum)
