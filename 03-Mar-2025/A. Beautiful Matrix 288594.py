# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

grid = []


for i in range(5):
    val = list(map(int, input().strip().split()))
    grid.append(val)

row, column = -1, -1
for i in range(len(grid)):
    if 1 in grid[i]:
        column = grid[i].index(1)
        row = i
        break  
distance = abs(2 - row) + abs(2 - column)
print(distance)