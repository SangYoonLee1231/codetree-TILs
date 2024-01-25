n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = 0


def search(r, c):
    global answer

    count = 0
    
    for i in range(3):
        for j in range(3):
            count += grid[r + i][c + j]
    
    answer = max(answer, count)


for i in range(n - 2):
    for j in range(n - 2):
        search(i, j)

print(answer)