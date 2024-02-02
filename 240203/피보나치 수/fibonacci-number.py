n = int(input())
dp = [-1] * (n + 1)

for i in range(1, n + 1):
    if n <= 2:
        dp[n] = 1
    else:
        dp[n] = dp[n - 1] + dp[n - 2]

print(dp[n])