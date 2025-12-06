f = open('advent3.in')

def findMaxDigitIdx(begin, end):
    maxDigit = -1
    maxDigitIdx = -1
    for i in range(begin, end):
        digit = int(line[i])
        if digit > maxDigit:
            maxDigit = digit
            maxDigitIdx = i
    assert(maxDigit != -1)
    assert(maxDigitIdx != -1)
    return maxDigit, maxDigitIdx

NUM_DIGIT = 12

total = 0
for line in f.readlines():
    line = line.strip()
    maxDigit = -1
    maxDigitIdx = -1
    for i in range(len(line)-1):
        digit = int(line[i])
        if digit > maxDigit:
            maxDigit = digit
            maxDigitIdx = i
    secondMaxDigit = -1
    for i in range(maxDigitIdx+1, len(line)):
        digit = int(line[i])
        if digit > secondMaxDigit:
            secondMaxDigit = digit

    curIdx = -1
    digits = []
    for d in range(NUM_DIGIT):
        maxDigit, maxDigitIdx = findMaxDigitIdx(curIdx+1, len(line)-(NUM_DIGIT-d-1))
        digits.append(str(maxDigit))
        curIdx = maxDigitIdx
    num = int(''.join(digits))

    print(num)
    total += num
print(total)