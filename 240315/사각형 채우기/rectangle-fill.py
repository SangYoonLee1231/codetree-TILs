n = int(input())

dp = [-1] * (n + 1)
dp[n] = 1


def dfs(curr_n):
    dp[curr_n] = 0

    for i in range(1, 3):
        next_n = curr_n + i

        if next_n > n:
            continue

        if dp[next_n] == -1:
            dfs(next_n)
        
        dp[curr_n] += dp[next_n]
        dp[curr_n] %= 10007


dfs(0)
print(dp[0])