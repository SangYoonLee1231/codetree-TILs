input_lst = list(map(int, input().split()))

dp = [0] * 10

for i in range(10):
    if i <= 1:
        dp[i] = input_lst[i]
        continue
     
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

for elem in dp:
    print(elem, end=" ")