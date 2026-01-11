f = open('advent4.in')

grid = []
for line in f.readlines():
    line = line.strip()
    grid.append(list(line))

dRow = [-1, -1, -1, 0, 1, 1, 1, 0]
dCol = [-1, 0, 1, 1, 1, 0, -1, -1]

N = len(grid)
M = len(grid[0])

res = 0
lastRemoved = -1
while lastRemoved != 0:
    lastRemoved = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            numRolls = 0
            if grid[i][j] != '@':
                continue
            for d in range(8):
                newRow = i+dRow[d]
                newCol = j+dCol[d]
                if 0 <= newRow < N and 0 <= newCol < M:
                    if grid[newRow][newCol] == '@':
                        numRolls += 1
            if numRolls < 4:
                res += 1
                lastRemoved += 1
                grid[i][j] = 'x'
                # print(i, j)
    print(lastRemoved)
print(res)