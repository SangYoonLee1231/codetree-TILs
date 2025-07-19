n, m = map(int, input().split())
snake_grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
grid = [
    [0] * m
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]

drs, dcs = [1, 0], [0, 1]


def dfs(r, c, depth):
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc

        if can_go(nr, nc):
            visited[nr][nc] = 1
            grid[nr][nc] = depth
            dfs(nr, nc, depth + 1)


def can_go(r, c):
    return in_range(r, c) and not visited[r][c] and snake_grid[r][c]


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m


dfs(0, 0, 1)

print(1 if grid[n - 1][m - 1] else 0)