n, t = tuple(map(int, input().split()))

lst_1st = list(map(int, input().split()))
lst_2nd = list(map(int, input().split()))
lst_3rd = list(map(int, input().split()))

lst = lst_1st + lst_2nd + lst_3rd

# 한 칸씩 밀고 당기기
def push_and_pull():
    temp = lst[3*n - 1]

    for i in range(3*n - 1, 0, -1):
        lst[i] = lst[i - 1]

    lst[0] = temp


for _ in range(t):
    push_and_pull()

# 출력
for i in range(3):
    for j in range(n):
        print(lst[i*n + j], end=' ')
    print()