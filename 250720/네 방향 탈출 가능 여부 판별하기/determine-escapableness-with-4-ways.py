from collections import deque

n, m = map(int, input().split())
snake_grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
drs, dcs = [0, 0, 1, -1], [1, -1, 0, 0]

visited = [
    [0] * m
    for _ in range(n)
]

q = deque()


def bfs():
    while q:
        r, c = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc

            if can_go(nr, nc):
                visited[nr][nc] = 1
                q.append((nr, nc))


def can_go(r, c):
    return in_range(r, c) and not visited[r][c] and snake_grid[r][c]


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m



visited[0][0] = 1
q.append((0, 0))
bfs()

print(visited[n - 1][m - 1])