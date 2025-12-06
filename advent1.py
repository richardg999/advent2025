f = open('advent1.in')

cur = 50
counter = 0
for line in f.readlines():
    line = line.strip()
    num = int(line[1:])
    isZero = (cur == 0)
    if line[0] == 'L':
        cur -= num
    else:
        cur += num
    # cur += 100
    # cur %= 100
    # if cur == 0:
    #     counter += 1

    # count zero at end but don't double-count
    while cur >= 100:
        cur -= 100
        counter += 1
        if cur == 0:
            counter -= 1
    if cur < 0 and isZero:
        counter -= 1
    while cur < 0:
        cur += 100
        counter += 1
    if cur == 0:
        counter += 1
    print(line, cur, counter)

    assert 0 <= cur < 100
print(counter)