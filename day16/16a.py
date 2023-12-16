import numpy as np
f = [list(x.strip()) for x in open('input', 'r')]
energized = np.zeros([len(f), len(f[0])])

RIGHT = (0,1)
LEFT = (0,-1)
UP = (-1,0)
DOWN = (1,0)
memo = set()


lase = [((0,-1), (0,1))]

while len(lase) > 0:
    n = []
    for l in lase:
        pos = l[0]
        direction = l[1]
        memo.add((pos, direction))
        if pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(f) and pos[1] < len(f[0]):
            energized[pos[0],pos[1]] = 1
        nextpos = (pos[0] + direction[0] , pos[1] + direction[1])
        if nextpos[0] < 0 or nextpos[1] < 0 or nextpos[0] >= len(f) or nextpos[1] >= len(f[0]):
            continue
        if f[nextpos[0]][nextpos[1]] == '.':
            n.append((nextpos, direction))
        elif f[nextpos[0]][nextpos[1]] == '/':
            if direction == UP:
                n.append((nextpos, RIGHT))
            elif direction == LEFT:
                n.append((nextpos, DOWN))
            elif direction == RIGHT:
                n.append((nextpos, UP))
            elif direction == DOWN:
                n.append((nextpos, LEFT))
            else:
                assert(False)
        elif f[nextpos[0]][nextpos[1]] == '\\':
            if direction == UP:
                n.append((nextpos, LEFT))
            elif direction == LEFT:
                n.append((nextpos, UP))
            elif direction == RIGHT:
                n.append((nextpos, DOWN))
            elif direction == DOWN:
                n.append((nextpos, RIGHT))
            else:
                assert(False)
        elif f[nextpos[0]][nextpos[1]] == '|':
            if direction == DOWN:
                n.append((nextpos, DOWN))
            elif direction == UP:
                n.append((nextpos, UP))
            elif direction == RIGHT:
                n.append((nextpos, UP))
                n.append((nextpos, DOWN))
            elif direction == LEFT:
                n.append((nextpos, UP))
                n.append((nextpos, DOWN))
            else:
                assert(False)
        elif f[nextpos[0]][nextpos[1]] == '-':
            if direction == LEFT:
                n.append((nextpos, LEFT))
            elif direction == RIGHT:
                n.append((nextpos, RIGHT))
            elif direction == UP:
                n.append((nextpos, LEFT))
                n.append((nextpos, RIGHT))
            elif direction == DOWN:
                n.append((nextpos, LEFT))
                n.append((nextpos, RIGHT))
            else:
                assert(False)
        else:
            assert(False)
    lase = [i for i in set(n) if i not in memo ]
print(energized)
print(np.sum(energized))
