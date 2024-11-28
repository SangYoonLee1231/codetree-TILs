n, b = tuple(map(int, input().split()))


def func(n, b):
    ans = []
    rem_lst = []

    while n >= b:
        rem_lst.append(n % b)
        n = n // b

    ans.append(str(n))

    rem_lst_len = len(rem_lst)
    for i in range(len(rem_lst) - 1, -1, -1):
        ans.append(str(rem_lst[i]))
    
    print(''.join(ans))


func(n, b)