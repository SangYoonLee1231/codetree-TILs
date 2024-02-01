from collections import deque

n, m = tuple(map(int, input().split()))

not_snake = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]


def in_range(r, c):
    return 0 <= r < n and 0 <= c < m


def bfs():
    while q:
        r, c = q.popleft()
        
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc

            if in_range(nr, nc) and not visited[nr][nc] and not_snake[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc))


q = deque()
visited[0][0] = 1
q.append((0, 0))
bfs()

print(visited[n - 1][m - 1])