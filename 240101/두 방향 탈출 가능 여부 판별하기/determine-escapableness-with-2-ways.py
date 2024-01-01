# n은 행, m은 열을 의미
n, m = tuple(map(int, input().split()))

snake = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0] * m
    for _ in range(n)
]

drs = [0, 1]
dcs = [1, 0]


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < m


def condition(r, c):
    if not in_range(r, c):
        return False
    if visited[r][c]:
        return False
    if snake[r][c]:
        return False
    return True


def dfs(r, c):
    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if condition(nr, nc):
            visited[nr][nc] = 1
            dfs(nr, nc)


visited[0][0] = 1
dfs(0, 0)
print(visited[n-1][m-1])