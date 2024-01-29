k, n = tuple(map(int, input().split()))
lst = []


def print_lst():
    for elem in lst:
        print(elem, end=' ')
    print()


def backtrack(curr_n):
    if curr_n == n + 1:
        print_lst()
        return
    
    for i in range(1, k + 1):
        if curr_n > 2 and lst[-1] == lst[-2] and lst[-1] == i:
            continue

        lst.append(i)
        backtrack(curr_n + 1)
        lst.pop()


backtrack(1)