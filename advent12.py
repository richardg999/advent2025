f = open('advent12.in')

shapes = []
N = 6
for i in range(N):
    f.readline()
    shape = []
    for i in range(3):
        row = f.readline()
        row = row.strip()
        shape.append(row)
    shapes.append(shape)
    f.readline()

shapeSizes = [0]*N
for shapeIdx in range(N):
    for i in range(3):
        for j in range(3):
            if shapes[shapeIdx][i][j] == '#':
                shapeSizes[shapeIdx] += 1

# return 0 if impossible, 1 if possible, -1 if unknown
def process(h, w, shapeCounts):
    minShapes = (h // 3) * (w // 3)
    total = 0
    for i in range(N):
        total += shapeCounts[i]*shapeSizes[i]
    if total >= h*w: # perfect utilization is impossible
        return 0
    if sum(shapeCounts) <= minShapes:
        return 1
    return -1

res = 0
for line in f.readlines():
    line = line.strip()
    elems = line.split()
    h, w = map(int, elems[0][:-1].split('x'))
    shapeCounts = list(map(int, elems[1:]))
    assert(len(shapeCounts) == N)
    verdict = process(h, w, shapeCounts)
    print(verdict, line)
    if verdict == -1:
        raise Exception('unknown')
    res += verdict
print(res)
