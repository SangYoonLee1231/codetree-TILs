n = int(input())
input_lst = list(map(int, input().split()))

lst = []


def print_median(n):
    temp_lst = sorted(lst)
    print(lst[n // 2], end=' ')


for i in range(n):
    lst.append(input_lst[i])

    if not i % 2:
        print_median(i + 1)