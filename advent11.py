from collections import deque

f = open('advent11.in')

graph = {}

nodes = set()

for line in f.readlines():
    line = line.strip()
    elems = line.split()
    parent = elems[0][:-1]
    children = elems[1:]
    graph[parent] = children
    nodes.add(parent)
    for c in children:
        nodes.add(c)

nodes = list(nodes)
nodeMap = {}
for i, name in enumerate(nodes):
    nodeMap[name] = i

# print(nodes)
N = len(nodes)
start = nodeMap['svr']
end = nodeMap['out']
g = [[] for i in range(N)]
for p, children in graph.items():
    g[nodeMap[p]] = [nodeMap[c] for c in children]

cur = [[0]*N for l in range(3)]
cur[0][start] = 1
res = 0
fft = nodeMap['fft']
dac = nodeMap['dac']
for step in range(N):
    nxt = [[0]*N for l in range(3)]
    for j in range(N):
        for l in range(3):
            if cur[l][j] > 0:
                if l == 0 and j == fft:
                    for c in g[j]:
                        nxt[l+1][c] += cur[l][j]
                elif l == 1 and j == dac:
                    for c in g[j]:
                        nxt[l+1][c] += cur[l][j]
                else:
                    for c in g[j]:
                        nxt[l][c] += cur[l][j]
    if nxt[2][end] != 0:
        print(f'found {nxt[2][end]} paths in {step+1} steps')
        res += nxt[2][end]
    # print(nxt)
    cur = nxt
print(res)