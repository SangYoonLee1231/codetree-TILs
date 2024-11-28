n, b = tuple(map(int, input().split()))


def func(n, b):
    rem_lst = []

    while n >= b:
        rem_lst.append(n % b)
        n = n // b

    rem_lst.append(n)

    for elem in rem_lst[::-1]:
        print(elem, end='')


func(n, b)