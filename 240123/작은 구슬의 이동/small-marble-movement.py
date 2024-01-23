n, t = tuple(map(int, input().split()))
r, c, d = input().split()
r, c = int(r), int(c)

drs = [-1, 0, 1, 0]
dcs = [0, 1, 0, -1]

mapper = {
    'U': 0,
    'R': 1,
    'D': 2,
    'L': 3,
}

dir_num = mapper[d]


def in_range(r, c):
    return r >= 1 and r <= n and c >= 1 and c <= n

def func():
    global r, c, dir_num

    for _ in range(t):
        nr, nc = r + drs[dir_num], c + dcs[dir_num]

        if in_range(nr, nc):
            r, c = nr, nc
        else:
            dir_num = (dir_num + 2) % 4
    
    return r, c

ans_r, ans_c = func()
print(ans_r, ans_c)