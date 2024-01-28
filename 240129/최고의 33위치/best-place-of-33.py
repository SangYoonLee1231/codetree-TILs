n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_coin = 0


def count_coins_in_square(r, c):
    coin = 0

    for i in range(3):
        for j in range(3):
            coin += grid[r + i][c + j]

    return coin


for i in range(n - 2):
    for j in range(n - 2):
        coin = count_coins_in_square(i, j)

        max_coin = max(max_coin, coin)

print(max_coin)