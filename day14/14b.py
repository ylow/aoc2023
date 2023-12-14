import copy
import hashlib
import pickle

def hash_anything(x):
    return hashlib.sha256(pickle.dumps(x)).hexdigest()


f = [list(x.strip()) for x in open('input', 'r')]

def rolln():
    global f
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == 'O':
                # roll it north
                ii = i - 1
                while ii >= 0:
                    if f[ii][j] == '.':
                        f[ii][j] = 'O'
                        f[ii+1][j] = '.'
                        ii -= 1
                    else:
                        break


def rolls():
    global f
    for i in reversed(range(len(f))):
        for j in range(len(f[i])):
            if f[i][j] == 'O':
                ii = i + 1
                while ii < len(f):
                    if f[ii][j] == '.':
                        f[ii][j] = 'O'
                        f[ii-1][j] = '.'
                        ii += 1
                    else:
                        break


def rollw():
    global f
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == 'O':
                jj = j - 1
                while jj >= 0:
                    if f[i][jj] == '.':
                        f[i][jj] = 'O'
                        f[i][jj+1] = '.'
                        jj -= 1
                    else:
                        break


def rolle():
    global f
    for i in range(len(f)):
        for j in reversed(range(len(f[i]))):
            if f[i][j] == 'O':
                jj = j + 1
                while jj < len(f[i]):
                    if f[i][jj] == '.':
                        f[i][jj] = 'O'
                        f[i][jj-1] = '.'
                        jj += 1
                    else:
                        break

def printb():
    print()
    for i in range(len(f)):
        print(''.join(f[i]))

def weight():
    w = 0
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] == 'O':
               w += len(f) - i 
    return w


hashes = {}
weights = {}
ctr = 0
c = []
for i in range(1000000000):
    rolln()
    rollw()
    rolls()
    rolle()
    h = hash_anything(f)
    if h in hashes:
        print(i+1, hashes[h], weights[h])
    else:
        hashes[h] = ctr
        weights[h] = weight()
        ctr += 1

print(len(hashes))
print(weight())
