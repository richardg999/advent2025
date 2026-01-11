f = open('advent7.in')

grid = []
for line in f.readlines():
    line = line.strip()
    grid.append(list(line))

counts = [[0]*len(grid[0]) for i in range(len(grid))]
for j in range(len(grid[0])):
    if grid[0][j] == 'S':
        counts[0][j] = 1

splits = 0
timelines = 1
for i in range(1, len(grid)):
    for j in range(0, len(grid[0])):
        if grid[i-1][j] == 'S' or grid[i-1][j] == '|':
            if grid[i][j] == '^':
                splits += 1
                timelines += counts[i-1][j]
                if j != 0:
                    grid[i][j-1] = '|'
                    counts[i][j-1] += counts[i-1][j]
                if j != len(grid[0])-1:
                    grid[i][j+1] = '|'
                    counts[i][j+1] += counts[i-1][j]
            elif grid[i][j] == '.' or grid[i][j] == '|':
                grid[i][j] = '|'
                counts[i][j] += counts[i-1][j]

print(splits)
print('timelines:', timelines)
# alternatively, you can count timelines via the number of counts on the bottom row

# for row in counts:
#     print(row)