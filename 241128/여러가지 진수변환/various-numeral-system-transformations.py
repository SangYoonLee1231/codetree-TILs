n, b = tuple(map(int, input().split()))


def func(n, b):
    rem_lst = []

    while n > 0:
        rem_lst.append(n % b)
        n = n // b

    for elem in rem_lst[::-1]:
        print(elem, end='')


func(n, b)