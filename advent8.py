f = open('advent8.in')

def dist(a, b):
    x1, y1, z1 = a
    x2, y2, z2 = b
    return (x1-x2)**2+(y1-y2)**2+(z1-z2)**2

points = []
for line in f.readlines():
    x, y, z = map(int, line.strip().split(','))
    points.append((x,y,z))

N = len(points)

dists = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        dists.append((dist(points[i], points[j]), i, j))
dists.sort()
# for d, i, j in dists:
#     print('dists:', d, i, j, points[i], points[j])

parents = [i for i in range(N)]

def find(i):
    root = parents[i]
    if root != i:
        parents[i] = find(root)
    return parents[i]

def union(i, j):
    jRoot = find(j)
    parents[jRoot] = find(i)

def connected(i, j):
    return find(i) == find(j)

connects = 0
lastConnects = -1
for d, i, j in dists:
    if not connected(i, j):
        lastConnects = points[i][0]*points[j][0]
    union(i, j)
    connects += 1
    # print('connected:', points[i], points[j])
    # if connects == 1000:
    #     break

segmentSizes = [0]*N
for i, p in enumerate(points):
    segmentSizes[find(i)] += 1

print(segmentSizes)
segmentSizes.sort(reverse=True)
res = segmentSizes[0]*segmentSizes[1]*segmentSizes[2]
print(res)
print('lastConnects:', lastConnects)
