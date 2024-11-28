n, k = tuple(map(int, input().split()))

lst = [0 for _ in range(n)]
ans = 0

for _ in range(k):
    a, b = tuple(map(int, input().split()))
    a, b = a - 1, b - 1

    for i in range(a, b + 1):
        lst[i] += 1
    
for elem in lst:
    ans = max(ans, elem)

print(ans)