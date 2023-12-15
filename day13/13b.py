f = [x.strip() for x in open("input", "r")]
f.append("")


def process_grid(g):
    for vmirror in range(1, len(g[0])):
        # insert mirror between col vmirror-1 and col vmirror
        mistakes = 0
        for i in range(len(g)):
            for j in range(vmirror):
                flip = vmirror + vmirror - j - 1
                if flip >= len(g[i]):
                    continue
                if g[i][j] != g[i][flip]:
                    mistakes += 1
        if mistakes == 1:
            return vmirror
        
    for hmirror in range(1, len(g)):
        # insert mirror between row hmirror-1 and row hmirror
        mistakes = 0
        for j in range(len(g[0])):
            for i in range(hmirror):
                flip = hmirror + hmirror - i - 1
                if flip >= len(g):
                    continue
                if g[i][j] != g[flip][j]:
                    mistakes += 1
        if mistakes == 1:
            return 100*hmirror


grid = []
s = 0
for row in f:
    if len(row) > 0:
        grid.append(list(row))
    else:
        s += process_grid(grid)
        grid = []
print(s)



