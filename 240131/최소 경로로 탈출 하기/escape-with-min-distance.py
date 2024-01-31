from collections import deque

n, m = tuple(map(int, input().split()))

not_snake = [
    list(map(int, input().split()))
    for _ in range(n)
]

dist_grid = [
    [-1 for _ in range(m)]
    for _ in range(n)
]

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]


def in_range(r, c):
    return 0 <= r < n and 0 <= c < m


def bfs():
    while q:
        r, c, dist = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc

            if in_range(nr, nc) and dist_grid[nr][nc] == -1 and not_snake[nr][nc]:
                q.append((nr, nc, dist + 1))
                dist_grid[nr][nc] = dist


q = deque()
q.append((0, 0, 1))
dist_grid[0][0] = 0
bfs()

print(dist_grid[n - 1][m - 1])