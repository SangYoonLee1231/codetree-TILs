n = int(input())

dp = [-1 for _ in range(n + 1)]
dp[n] = 1


def dfs(curr_n):
    dp[curr_n] = 0

    for i in range(2, 4):
        next_n = curr_n + i

        if next_n > n:
            continue

        if dp[next_n] == -1:
            dfs(next_n)

        dp[curr_n] += dp[next_n]


dfs(0)
print(dp[0])