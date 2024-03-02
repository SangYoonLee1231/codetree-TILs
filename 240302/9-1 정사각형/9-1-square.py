n = int(input())

num = 9

for _ in range(n):
    for _ in range(n):
        num = (num - 1) % 9
        print(num + 1, end="")
    print()