n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = 0


def search_row(r):
    global answer

    max_count = 1
    count = 1

    for c in range(n - 1):
        if grid[r][c] == grid[r][c + 1]:
            count += 1
        else:
            count = 1
        
        max_count = max(max_count, count)
    
    if max_count >= m:
        answer += 1


def search_col(c):
    global answer

    max_count = 1
    count = 1

    for r in range(n - 1):
        if grid[r][c] == grid[r + 1][c]:
            count += 1
        else:
            count = 1

        max_count = max(max_count, count)
    
    if max_count >= m:
        answer += 1



for i in range(n):
    search_row(i)

for i in range(n):
    search_col(i)

print(answer)