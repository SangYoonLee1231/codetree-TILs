lst = [
    input()
    for _ in range(3)
]

min_len = 20
max_len = 0

for elem in lst:
    length = len(elem)
    min_len = min(min_len, length)
    max_len = max(max_len, length)

answer = max_len - min_len
print(answer)