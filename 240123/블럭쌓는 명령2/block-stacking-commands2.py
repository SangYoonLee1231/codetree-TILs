n, k = tuple(map(int, input().split()))

lst = [0] * (n + 1)

answer = 0

for _ in range(k):
    start, end = tuple(map(int, input().split()))
    
    for idx in range(start, end + 1):
        lst[idx] += 1

for elem in lst:
    answer = max(answer, elem)

print(answer)