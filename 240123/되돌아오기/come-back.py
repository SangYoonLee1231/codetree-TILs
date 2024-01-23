n = int(input())

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

mapper = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
}

x, y = 0, 0
count = 0
flag = False

for _ in range(n):
    dir_str, dist = input().split()
    dist = int(dist)

    dir_num = mapper[dir_str]
    dx, dy = dxs[dir_num], dys[dir_num]

    for _ in range(dist):
        x, y = x + dx, y + dy

        if not flag:
            count += 1

        if x == 0 and y == 0 and not flag:
            flag = True
            print(count)

if not flag:
    print(-1)