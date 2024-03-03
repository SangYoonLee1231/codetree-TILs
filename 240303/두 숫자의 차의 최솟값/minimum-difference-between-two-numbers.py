import sys

n = int(input())
lst = list(map(int, input().split()))

answer = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):
        diff = lst[j] - lst[i]
        answer = min(answer, diff)

print(answer)