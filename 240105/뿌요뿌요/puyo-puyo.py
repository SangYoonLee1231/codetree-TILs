n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0] * n
    for _ in range(n)
]

cnt = 0
max_block_cnt = 0

explode_cnt = 0

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n


def can_go(r, c):
    if not in_range(r, c):
        return False
    if visited[r][c]:
        return False
    return True


def dfs(r, c):
    global cnt

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if can_go(nr, nc) and grid[r][c] == grid[nr][nc]:
            visited[nr][nc] = 1
            cnt += 1
            dfs(nr, nc)


for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt = 1
            visited[i][j] = 1
            dfs(i, j)

            if cnt >= 4:
                explode_cnt += 1

            max_block_cnt = max(max_block_cnt, cnt)

print(explode_cnt, max_block_cnt)