f = open('advent2.in')

def sumRange(r):
    begin, end = map(int, r.split('-'))
    total = 0
    for i in range(begin, end+1):
        numStr = str(i)
        for k in range(2, len(numStr)+1):
            if len(numStr) % k == 0:
                example = numStr[:len(numStr)//k]
                matches = True
                for j in range(1, k):
                    if numStr[j*len(numStr)//k:(j+1)*len(numStr)//k] != example:
                        matches = False
                        break
                if matches:
                    print(i)
                    total += i
                    break
    return total

rs = f.readline().strip().split(',')
res = sum([sumRange(r) for r in rs])
print(res)