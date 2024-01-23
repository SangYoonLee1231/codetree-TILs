n = int(input())

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

dict = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
}

x, y = 0, 0

for _ in range(n):
    dir_str, dist = input().split()
    dist = int(dist)

    dir_num = dict[dir_str]

    x += dxs[dir_num] * dist
    y += dys[dir_num] * dist

print(x, y)