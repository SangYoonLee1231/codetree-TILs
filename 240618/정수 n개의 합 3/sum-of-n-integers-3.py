import sys

n, k = tuple(map(int, input().split()))

grid = [[0] * (n + 1)] + [
    [0] + list(map(int, input().split()))
    for _ in range(n)
]

prefix_sum = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

answer = -sys.maxsize

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + grid[i][j]

# k*k 사각형 중 최대합 찾기
for i in range(k, n + 1):
    for j in range(k, n + 1):
        temp = prefix_sum[i][j] - prefix_sum[i-k][j] - prefix_sum[i][j-k] + prefix_sum[i-k][j-k]
        answer = max(answer, temp)

print(answer)