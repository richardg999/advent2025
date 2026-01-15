from collections import deque

f = open('advent10.in')

def flip(c):
    if c == '.':
        return '#'
    else:
        return '.'

# diagram = ".##.", buttons = [[3], [1,3], ...]
def process(diagram, buttons):
    q = deque()
    N = len(diagram)
    q.append((['.']*N, 0))
    seen = set()
    while len(q) != 0:
        elem, c = q.popleft()
        s = ''.join(elem)
        # print(s, c)
        if s in seen:
            continue

        seen.add(s)
        if s == diagram:
            return c
        for b in buttons:
            e = elem.copy()
            for num in b:
                e[num] = flip(e[num])
                # print('flipping', b, num, e[num], flip(e[num]))
            q.append((e, c+1))
            # print('appending', e, c+1)
    raise Exception("Impossible")

# def process2(voltage, buttons):
#     if len(buttons) == 0:
#         if any([v > 0 for v in voltage]):
#             return -1
#         else:
#             assert(not (any([v < 0 for v in voltage])))
#             return 0
#     # first find guaranteed cases
#     for voltIdx, volt in enumerate(voltage):
#         if volt == 0:
#             continue
#         numButtons = 0
#         lastButtonIdx = -1
#         for buttonIdx, button in enumerate(buttons):
#             if voltIdx in button:
#                 numButtons += 1
#                 lastButtonIdx = buttonIdx
#         if numButtons == 0:
#             return -1
#         assert(numButtons != 0)
#         if numButtons == 1:
#             newVoltage = voltage.copy()
#             assert(lastButtonIdx != -1)
#             for b in buttons[lastButtonIdx]:
#                 newVoltage[b] -= volt
#                 if newVoltage[b] < 0:
#                     return -1
#                 assert(newVoltage[b] >= 0)
#             newButtons = buttons[0:lastButtonIdx]+buttons[lastButtonIdx+1:]
#             res = process2(newVoltage, newButtons)
#             if res == -1:
#                 return -1
#             print('volt', volt, ', voltage', voltage, ', newVoltage', newVoltage, ', newButtons', newButtons)
#             return volt+res
#     # print('process2', voltage, buttons)

#     # idea: take the tightest constraint and fully apply the largest button that touches that constraint
#     for minVoltIdx, minVolt in sorted(enumerate(voltage), key=lambda x: x[1]):
#         for buttonIdx, button in sorted(enumerate(buttons), key=lambda x: -len(x[1])):
#             if minVoltIdx in button:
#                 newVoltage = voltage.copy()
#                 forceContinue = False
#                 for b in buttons[buttonIdx]:
#                     newVoltage[b] -= minVolt
#                     if newVoltage[b] < 0:
#                         forceContinue = True
#                         break
#                     assert(newVoltage[b] >= 0)
#                 if forceContinue:
#                     continue
#                 newButtons = buttons[0:buttonIdx] + buttons[buttonIdx+1:]
#                 res = process2(newVoltage, newButtons)
#                 if res == -1:
#                     continue
#                 print('minVolt', minVolt, ', voltage', voltage, ', newVoltage', newVoltage, ', buttonIdx', buttonIdx)
#                 return minVolt + res
#     return -1

from scipy.optimize import linprog

def process2(voltage, buttons):
    N = len(buttons)
    M = len(voltage)
    c = [1]*N
    # each row is an equation, and the 1s represent relevance of a button
    A_eq = [[0]*N for i in range(M)]
    b_eq = voltage
    for i, button in enumerate(buttons):
        for b in button:
            A_eq[b][i] = 1
    # print(A_eq)
    # print(b_eq)
    A_ub = [[0]*N for i in range(N)]
    for i in range(N):
        A_ub[i][i] = -1
    b_ub = [0]*N
    res = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, integrality=1)
    return int(res.fun)



res = 0
for line in f.readlines():
    line = line.strip()
    elems = line.split()
    # diagram = elems[0]
    # diagram = diagram[1:-1]
    buttons = elems[1:-1]
    buttons = [list(map(int, button[1:-1].split(','))) for button in buttons]
    voltage = list(map(int, elems[-1][1:-1].split(',')))
    val = process2(voltage, buttons)
    if val == -1:
        print('Cannot solve', line)
    print(val)
    res += val
print('res', res)
