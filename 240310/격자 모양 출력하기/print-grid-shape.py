n, m = tuple(map(int, input().split()))

grid = [
    [0] * n
    for _ in range(n)
]

for _ in range(m):
    r, c = tuple(map(int, input().split()))
    grid[r - 1][c - 1] = r * c

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()