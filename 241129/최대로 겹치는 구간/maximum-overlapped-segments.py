OFFSET = 100

n = int(input())

lst = [0 for _ in range(201)]

for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))
    x1, x2 = x1 + OFFSET, x2 + OFFSET

    for i in range(x1, x2):
        lst[i] += 1


print(max(lst))