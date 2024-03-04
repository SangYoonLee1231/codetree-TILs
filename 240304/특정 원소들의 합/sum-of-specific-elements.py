grid = [
    list(map(int, input().split()))
    for _ in range(4)
]

answer = 0

for i in range(4):
    for j in range(i + 1):
        answer += grid[i][j]

print(answer)