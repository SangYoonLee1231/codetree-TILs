from collections import deque

n, m = tuple(map(int, input().split()))
q = deque()

no_snake = [
    list(map(int, input().split()))
    for _ in range(n)
]

shortest_dist = [
    [0] * m
    for _ in range(n)
]

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]


def push(r, c, dist):
    shortest_dist[r][c] = dist
    q.append((r, c, dist))


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m


def can_go(r, c):
    if not in_range(r, c):
        return False
    if not no_snake[r][c]:
        return False
    if shortest_dist[r][c]:
        return False
    return True


def bfs():
    while q:
        r, c, dist = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                push(nr, nc, dist + 1)



push(0, 0, 0)
bfs()

answer = shortest_dist[n - 1][m - 1]
print(answer if answer else -1)