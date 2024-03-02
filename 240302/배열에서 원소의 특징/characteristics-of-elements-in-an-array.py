lst = list(map(int, input().split()))

idx = -1

for i in range(10):
    if lst[i] % 3 == 0:
        idx = i
        break

answer = lst[idx - 1]
print(answer)