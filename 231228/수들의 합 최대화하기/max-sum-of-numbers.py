n = int(input())
visited_row = [False] * (n)
visited_col = [False] * (n)
answer = 0
selected_lst = []

lst = [
    list(map(int, input().split()))
    for _ in range(n)
]


def calc_sum():
    global answer

    curr_sum = 0
    
    for elem in selected_lst:
        curr_sum += elem

    answer = max(answer, curr_sum)


def choose(selected_num, row, col):
    if selected_num == n:
        calc_sum()
        return

    for r in range(n):
        for c in range(n):
            if visited_row[r] or visited_col[c]:
                continue
            
            visited_row[r] = True
            visited_col[c] = True
            selected_lst.append(lst[r][c])

            choose(selected_num + 1, r, c)

            selected_lst.pop()
            visited_col[c] = False
            visited_row[r] = False


choose(0, 0, 0)
print(answer)