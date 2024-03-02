n = int(input())

lst = []

for i in range(1, n + 1):
    if i % 2:
        lst.append("* " * (n - i // 2))
    else:
        lst.append("* " * (i // 2))


for i in range(n):
    print(lst[i])

for i in range(n - 1, -1, -1):
    print(lst[i])