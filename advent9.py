f = open('advent9.in')

def dist(a, b):
    x1, y1 = a
    x2, y2 = b
    return (abs(x1-x2)+1)*(abs(y1-y2)+1)

xAxes = set()
yAxes = set()
points = []
for line in f.readlines():
    line = line.strip()
    x, y = map(int, line.split(','))
    points.append((x,y))
    xAxes.add(x)
    yAxes.add(y)
    assert x >= 0
    assert y >= 0
xAxes = sorted(xAxes)
yAxes = sorted(yAxes)
xAxisMap = {}
yAxisMap = {}
for i, x in enumerate(xAxes):
    xAxisMap[x] = i
for i, y in enumerate(yAxes):
    yAxisMap[y] = i
grid = [[0]*len(yAxes) for i in range(len(xAxes))]
prevP = points[-1]
for p in points:
    pX = xAxisMap[p[0]]
    pY = yAxisMap[p[1]]
    prevPX = xAxisMap[prevP[0]]
    prevPY = yAxisMap[prevP[1]]
    if pX == prevPX:
        for j in range(min(pY, prevPY), max(pY, prevPY)+1):
            grid[pX][j] = 1
    elif pY == prevPY:
        for i in range(min(pX, prevPX), max(pX, prevPX)+1):
            grid[i][pY] = 1
    else:
        assert(False)
    prevP = p

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

import sys

sys.setrecursionlimit(2000000)

def flood(a, b):
    if a < 0 or a >= len(grid):
        return
    if b < 0 or b >= len(grid[0]):
        return
    if grid[a][b] == 1 or grid[a][b] == 2:
        return
    grid[a][b] = 2
    for d in range(4):
        newRow = a+dRow[d]
        newCol = b+dCol[d]
        flood(newRow, newCol)


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i != 0 and j != 0 and i != len(grid)-1 and j != len(grid[0])-1:
            continue
        flood(i, j)

# for row in grid:
#     print(row)

def check(p1, p2):
    p1X = xAxisMap[p1[0]]
    p1Y = yAxisMap[p1[1]]
    p2X = xAxisMap[p2[0]]
    p2Y = yAxisMap[p2[1]]
    for i in range(min(p1X, p2X), max(p1X, p2X)+1):
        for j in range(min(p1Y, p2Y), max(p1Y, p2Y)+1):
            if grid[i][j] == 2:
                return False
    return True

N = len(points)
res = 0
for i in range(N):
    for j in range(i+1, N):
        d = dist(points[i], points[j])
        if d > res and check(points[i], points[j]):
            res = d

print(res)
