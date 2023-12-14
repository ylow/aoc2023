f = [list(x.strip()) for x in open('input', 'r')]

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

w = 0
for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == 'O':
           w += len(f) - i 
    print(''.join(f[i]))

print(w)
