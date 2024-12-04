# 0 = 색 없음 / -1 = 흰색 / 1 = 검은색

n = int(input())

order = [
    list(input().split())
    for _ in range(n)
]

lst_color = [0 for _ in range(200001)]
lst_white_cnt = [0 for _ in range(200001)]
lst_black_cnt = [0 for _ in range(200001)]


def move_and_paint():
    curr = 100000

    for i in range(n):
        x = int(order[i][0])
        dir_x = order[i][1]

        if dir_x == 'L':
            for idx in range(curr - x + 1, curr + 1):
                lst_color[idx] = -1
                lst_white_cnt[idx] += 1
            curr -= (x - 1)
        
        if dir_x == 'R':
            for idx in range(curr, curr + x):
                lst_color[idx] = 1
                lst_black_cnt[idx] += 1
            curr += (x - 1)


def count():
    white = 0
    black = 0
    gray = 0

    for i in range(200001):
        if lst_white_cnt[i] >= 2 and lst_black_cnt[i] >= 2:
            gray += 1
            continue
        if lst_color[i] == -1:
            # 흰색
            white += 1
        if lst_color[i] == 1:
            # 검색
            black += 1
    
    return white, black, gray


move_and_paint()
white, black, gray = count()

print(white, black, gray)