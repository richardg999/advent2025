f = open('advent5.in')

def testRanges(rs, val):
    for r in rs:
        beg, end = r
        if beg <= val <= end:
            return True
    return False

rs = []
processRanges = True
res = 0
for line in f.readlines():
    line = line.strip()
    if line == '':
        processRanges = False
        continue
    if processRanges:
        beg, end = map(int, line.split('-'))
        rs.append((beg, end))
    else:
        # val = int(line)
        # if testRanges(rs, val):
        #     res += 1
        #     print(val)
        continue
# print(res)

def processIntervals(rs):
    rs.sort()
    curEnd = -1 # inclusive
    total = 0
    for r in rs:
        beg, end = r
        if beg > curEnd:
            curEnd = beg
        contrib = max(0, end - curEnd + 1)
        curEnd = max(curEnd, end+1)
        total += contrib
        print(r, contrib)
    return total

res = processIntervals(rs)
print(res)