n = int(input())
max_count = 0

loc_list = [
    list(map(int, input().split()))
    for _ in range(n)
]

dir_list = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = tuple(map(int, input().split()))


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n


# (r-1)행 (c-1)열 칸에서 다음으로 이동할 수 있는 칸 탐색하는 함수
def search(cr, cc, count):
    global r, c, max_count

    loc_num = loc_list[cr][cc]
    dir_num = dir_list[cr][cc] - 1

    max_count = max(count, max_count)

    i = 1
    while True:
        nr, nc = cr + (i * dr[dir_num]), cc + (i * dc[dir_num])
        if not in_range(nr, nc):
            return
        if loc_num < loc_list[nr][nc]:
            search(nr, nc, count + 1)
        i += 1


search(r-1, c-1, 0)
print(max_count)