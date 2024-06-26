n = int(input())
sections = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

checked = [0] * 200001
sum_val = [0] * 200001

for start, end in sections:
    checked[start] += 1
    checked[end] -= 1

for i in range(1, 200001):
    sum_val[i] += checked[i] + sum_val[i - 1]

print(max(sum_val))