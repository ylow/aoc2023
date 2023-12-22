import numpy as np
import scipy 
lines = [x.strip() for x in open("input",'r')]

bricks = []
for l in lines:
    start,end = l.split('~')
    start = np.array([int(i) for i in start.split(',')])
    end = np.array([int(i) for i in end.split(',')])
    # we will normalize it so start <= end
    if not (start <= end).all():
        start, end = end, start
    assert((start <= end).all())
    bricks.append((start, end))

def interp(brick):
    start, end = brick
    delta = np.sign(end - start)
    dist = np.sum(end - start)
    i = 0
    s = np.copy(start)
    yield(s)
    while i < dist:
        s += delta
        i += 1
        yield(s)

# sort bricks by z 
bricks = sorted(bricks, key = lambda x: x[0][2])
world = {}
for i, b in enumerate(bricks):
    for coord in interp(b):
        world[tuple(coord)] = i + 1

def has_brick_at(coord, world):
    t = tuple(coord)
    if t in world:
        return world[t]
    return 0

ZDOWN = np.array([0,0,-1])

def brick_can_fall(b, bid, world):
    if b[0][2] == 1:
        return False
    for i in interp(b):
        brickat = has_brick_at(i + ZDOWN, world)
        if brickat == 0 or brickat == bid + 1:
            continue
        else:
            return False
    return True

def remove_brick(b, world):
    for i in interp(b):
        t = tuple(i)
        world[t] = 0

def put_brick(b, bid, world):
    for i in interp(b):
        t = tuple(i)
        world[t] = bid + 1

while True:
    falling = False
    for b in range(len(bricks)):
        while brick_can_fall(bricks[b], b, world):
            falling = True
            remove_brick(bricks[b], world)
            bricks[b] = (bricks[b][0] + ZDOWN, bricks[b][1] + ZDOWN)
            put_brick(bricks[b], b, world)
    if falling == False:
        break

#print(bricks)

removable_bricks = 0
# check for removable brick
for b in range(len(bricks)):
    remove_brick(bricks[b], world)
    falling = False
    for b2 in range(len(bricks)):
        if b2 != b:
            if brick_can_fall(bricks[b2], b2, world):
                falling = True
                break
    if falling == False:
        removable_bricks += 1
    put_brick(bricks[b],b, world)

print(removable_bricks)
