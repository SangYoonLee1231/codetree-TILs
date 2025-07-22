n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
max_sum = 0

for i in range(n - k):
    temp_sum = 0

    for j in range(k):
        temp_sum += arr[i + j]

    max_sum = max(max_sum, temp_sum)

print(max_sum)