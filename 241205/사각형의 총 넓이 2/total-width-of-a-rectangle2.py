OFFEST = 100

n = int(input())

inputs = [
    list(map(int, input().split()))
    for _ in range(n)
]

grid = [
    [0] * 201
    for _ in range(201)
]

for i in range(n):
    x1, y1, x2, y2 = inputs[i]
    x1, y1, x2, y2 = x1 + OFFEST, y1 + OFFEST, x2 + OFFEST, y2 + OFFEST

    for i in range(x1, x2):
        for j in range(y1, y2):
            grid[i][j] = 1

# 출력
answer = 0

for i in range(201):
    answer += sum(grid[i])

print(answer)