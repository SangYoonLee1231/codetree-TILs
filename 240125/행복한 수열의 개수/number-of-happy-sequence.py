n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

line_count = 0
answer = 0
cnt = 1

for i in range(n):
    for j in range(n - 1):
        if grid[i][j] == grid[i][j + 1]:
            cnt += 1
        else: 
            line_count = max(line_count, cnt)
            cnt = 1    
    
    if line_count >= m:
        answer += 1
    line_count = 0

cnt = 1

for i in range(n):
    for j in range(n - 1):
        if grid[j][i] == grid[j + 1][i]:
            cnt += 1
        else: 
            line_count = max(line_count, cnt)
            cnt = 1
    
    if line_count >= m:
        answer += 1
    line_count = 0

print(answer)