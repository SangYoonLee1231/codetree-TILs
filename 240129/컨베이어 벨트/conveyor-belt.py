n, t = tuple(map(int, input().split()))

lst_up = list(map(int, input().split()))
lst_down = list(map(int, input().split()))

lst = lst_up + lst_down

# 한 칸씩 밀고 당기기
def push_and_pull():
    temp = lst[2*n - 1]

    for i in range(2*n - 1, 0, -1):
        lst[i] = lst[i - 1]

    lst[0] = temp


for _ in range(t):
    push_and_pull()

# 출력
for i in range(2):
    for j in range(n):
        print(lst[i*n + j], end=' ')
    print()