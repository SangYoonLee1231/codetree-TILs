n = int(input())
lst = [
    int(input())
    for _ in range(n)
]
length = n

for _ in range(2):
    s, e = tuple(map(int, input().split()))
    s, e = s - 1, e - 1
    s, e = (n - length) + s, (n - length) + e

    temp = [-1] * length

    temp_idx = length - 1
    for i in range(n - 1, n - 1 - length, -1):
        if i < s or i > e:
            temp[temp_idx] = lst[i]
            temp_idx -= 1
    
    for i in range(length):
        lst[i] = temp[i]
    
    length = length - (e - s + 1)

print(length)

answer = []

for i in range(length, -1, -1):
    if not lst[i] == -1:
        answer.append(lst[i])

for i in range(len(answer) - 1, -1, -1):
    print(answer[i])