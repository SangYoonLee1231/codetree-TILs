n = int(input())

print("* " * n)

for i in range(1, n - 1):
    print("* " * i, end="")
    print("  " * (n - 1 - i), end="")
    print("* ")

print("* " * n)