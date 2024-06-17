import sys

n, k = tuple(map(int, input().split()))
lst = list(map(int, input().split()))

answer = -sys.maxsize

prefix_sum = [0] * n
prefix_sum[0] = lst[0]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + lst[i]

for i in range(k, n):
    answer = max(answer, prefix_sum[i] - prefix_sum[i - k])

print(answer)