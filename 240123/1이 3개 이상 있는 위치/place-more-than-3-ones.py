n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

drs = [0, 1, 0, -1]
dcs = [1, 0, -1, 0]

answer = 0


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n


def search(r, c):
    count = 0

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc

        if in_range(nr, nc):
            count += grid[nr][nc]

    if count >= 3:
        return 1
    return 0    


for r in range(n):
    for c in range(n):
        answer += search(r, c)

print(answer)