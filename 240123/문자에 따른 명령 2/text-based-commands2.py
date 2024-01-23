cmd = input()

cmd_lst = list(cmd)

x, y = 0, 0

dxs = [0 ,1, 0, -1]
dys = [1, 0, -1, 0]

dir_num = 0

for elem in cmd_lst:
    if elem == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif elem == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x += dxs[dir_num]
        y += dys[dir_num]

print(x, y)