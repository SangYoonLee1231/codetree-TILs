from collections import deque

n = int(input())
r1, c1, r2, c2 = tuple(map(int, input().split()))
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
q = deque()

visited = [
    [0] * n
    for _ in range(n)
]

drs = [-2, -1, 1, 2, 2, 1, -1, -2]
dcs = [-1, -2, -2, -1, 1, 2, 2, 1]


def move(r, c, cnt):
    q.append((r, c, cnt))
    visited[r][c] = 1


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n


def can_move(nr, nc):
    if not in_range(nr, nc):
        return False
    if visited[nr][nc]:
        return False
    return True


def bfs():
    while q:
        r, c, cnt = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_move(nr, nc):
                move(nr, nc, cnt + 1)
                if nr == r2 and nc == c2:
                    return cnt + 1


move(r1, c1, 0)
answer = bfs()
print(answer if answer else -1)