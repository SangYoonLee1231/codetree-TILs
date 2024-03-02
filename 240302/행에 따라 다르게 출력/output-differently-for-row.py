n = int(input())

num = 0
for i in range(1, n + 1):
    for _ in range(n):
        if i % 2:
            num += 1
        else:
            num += 2
        print(num, end=" ")

    print()