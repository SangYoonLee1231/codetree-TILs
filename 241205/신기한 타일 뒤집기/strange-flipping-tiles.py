# 0 = 회색 , -1 = 흰색, 1 = 검은색

n = int(input())

order = [
    list(input().split())
    for _ in range(n)
]

lst = [0 for _ in range(200001)]


def move_and_flip():
    curr_pos = 100000

    for i in range(n):
        x = int(order[i][0])
        dir_pos = order[i][1]

        if dir_pos == 'L':
            for idx in range(curr_pos - x + 1, curr_pos + 1):
                lst[idx] = -1
            curr_pos -= (x - 1)
        if dir_pos == 'R':
            for idx in range(curr_pos, curr_pos + x):
                lst[idx] = 1
            curr_pos += (x - 1)


def count_white_and_black():
    count_white = 0
    count_black = 0

    for elem in lst:
        if elem == -1:
            count_white += 1
        if elem == 1:
            count_black += 1
    
    return count_white, count_black


move_and_flip()
white, black = count_white_and_black()
print(white, black)

