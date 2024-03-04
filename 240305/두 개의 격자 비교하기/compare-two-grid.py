n, m = tuple(map(int, input().split()))

grid_one = [
    list(map(int, input().split()))
    for _ in range(n)
]

grid_two = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = [
    [0] * m
    for _ in range(n)
]

for r in range(n):
    for c in range(m):
        if grid_one[r][c] == grid_two[r][c]:
            continue
        answer[r][c] = 1

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=" ")
    print()