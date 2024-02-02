# Tabulation
# n = int(input())
# dp = [-1] * (n + 1)

# for i in range(1, n + 1):
#     if i <= 2:
#         dp[i] = 1
#     else:
#         dp[i] = dp[i - 1] + dp[i - 2]

# print(dp[n])


# Memoization
n = int(input())
dp = [-1] * (n + 1)


def dp_func(n):
    if dp[n] != -1:
        return dp[n]

    if n <= 2:
        dp[n] = 1
        return dp[n]
    
    dp[n] = dp_func(n - 1) + dp_func(n - 2)
    return dp[n]


dp_func(n)
print(dp[n])