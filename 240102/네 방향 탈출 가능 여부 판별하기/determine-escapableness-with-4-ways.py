from collections import deque
# popleft, append

n, m = tuple(map(int, input().split()))

snake = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0] * m
    for _ in range(n)
]

q = deque()

# 우, 하, 좌, 상
drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]


def push(r, c):
    q.append((r, c))
    visited[r][c] = 1


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m


def can_move(r, c):
    if not in_range(r, c):
        return False
    if visited[r][c]:
        return False
    if not snake[r][c]:
        return False
    return True


def bfs():
    while q:
        r, c = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_move(nr, nc):
                push(nr, nc)


push(0, 0)
bfs()
print(visited[n - 1][m - 1])