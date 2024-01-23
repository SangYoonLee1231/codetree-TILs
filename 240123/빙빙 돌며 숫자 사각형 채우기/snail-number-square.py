n, m = tuple(map(int, input().split()))

grid = [
    [0] * m
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]

dir_num = 0

r, c = 0, 0
grid[r][c] = 1
visited[0][0] = True


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m


for i in range(2, n * m + 1):
    nr, nc = r + drs[dir_num], c + dcs[dir_num]

    if in_range(nr, nc) and not visited[nr][nc]:
        pass
    else:
        dir_num = (dir_num + 1) % 4
        nr, nc = r + drs[dir_num], c + dcs[dir_num]

    grid[nr][nc] = i
    visited[nr][nc] = True

    r, c = nr, nc

for r in range(n):
    for c in range(m):
        print(grid[r][c], end=' ')
    print()