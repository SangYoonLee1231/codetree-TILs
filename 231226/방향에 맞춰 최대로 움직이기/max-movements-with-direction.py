n = int(input())

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


# (r-1)행 (c-1)열 칸에서 다음으로 이동할 수 있는 칸을 반환하는 함수
def search(r, c):
    loc_num = loc_list[r][c]
    dir_num = dir_list[r][c] - 1

    i = 1
    while in_range(r, c):
        nr, nc = r + (i * dr[dir_num]), c + (i * dc[dir_num])
        if in_range(nr, nc) and loc_num < loc_list[nr][nc]:
            return 1 + search(nr, nc)
        i += 1
        r, c = nr, nc

    return 0


print(search(r-1, c-1) + 1)