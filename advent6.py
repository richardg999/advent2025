f = open('advent6.in')

# lines = []
# for line in f.readlines():
#     line = line.strip()
#     lines.append(line.split())

# N = len(lines[0])
# res = 0
# for i in range(N):
#     op = lines[-1][i]
#     if op == '+':
#         base = 0
#         for j in range(len(lines)-1):
#             base += int(lines[j][i])
#     else:
#         base = 1
#         for j in range(len(lines)-1):
#             base *= int(lines[j][i])
#     print(base)
#     res += base
# print(res)

lines = []
for line in f.readlines():
    line = line[:-1]
    lines.append(line)
M = len(lines[0])
for line in lines[:-1]:
    assert(len(line) == M), (len(line), M, line)

numGrid = []
ops = lines[-1].split()
N = len(ops)
nums = []

for col in range(len(lines[0])):
    curNum = ''
    for row in range(len(lines)-1):
        if lines[row][col] != ' ':
            curNum += lines[row][col]
    if curNum == '':
        numGrid.append(nums)
        nums = []
    else:
        nums.append(int(curNum))

numGrid.append(nums)
assert(len(numGrid) == N)
res = 0
for i in range(N):
    if ops[i] == '+':
        base = 0
        for num in numGrid[i]:
            base += num
    else:
        base = 1
        for num in numGrid[i]:
            base *= num
    res += base
    print(base)
print(res)
