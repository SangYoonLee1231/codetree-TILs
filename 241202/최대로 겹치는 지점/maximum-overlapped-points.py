n = int(input())

segments = [
    list(map(int, input().split()))
    for _ in range(n)
]

checked = [0 for _ in range(101)]

for x1, x2 in segments:
    for idx in range(x1, x2 + 1):
        checked[idx] += 1

print(max(checked))