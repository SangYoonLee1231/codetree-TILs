n, m = tuple(map(int, input().split()))

lst = [
    list(map(int, input().split()))
    for _ in range(m)
]

grid = [
    [0] * (n)
    for _ in range(n)
]

for elem in lst:
    r, c = elem
    r, c = r - 1, c - 1

    grid[r][c] = 1

for r in range(n):
    for c in range(n):
        print(grid[r][c], end=' ')
    print()