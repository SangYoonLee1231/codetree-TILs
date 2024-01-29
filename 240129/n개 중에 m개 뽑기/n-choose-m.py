n, m = tuple(map(int, input().split()))
lst = []
# used = [False] * (n + 1)


def print_lst():
    for elem in lst:
        print(elem, end=' ')
    print()


def backtrack(curr_n, last_num):
    if curr_n >= m:
        print_lst()
        return

    for i in range(last_num + 1, n + 1):
        # if curr_n >= 1 and lst[-1] >= i:
        #     continue

        # if not used[i]:
            lst.append(i)
            # used[i] = True
            backtrack(curr_n + 1, i)
            # used[i] = False
            lst.pop()



backtrack(0, 0)