k, n = tuple(map(int, input().split()))
lst = []


def print_lst():
    for elem in lst:
        print(elem, end = ' ')
    print()
    return


def backtrack(curr_n):
    if curr_n == n:
        print_lst()
        return

    for i in range(1, k + 1):
        lst.append(i)
        backtrack(curr_n + 1)
        lst.pop()


backtrack(0)