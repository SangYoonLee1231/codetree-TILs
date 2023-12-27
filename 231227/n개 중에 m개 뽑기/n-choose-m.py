n, m = tuple(map(int, input().split()))
ans = []


def print_num():
    for elem in ans:
        print(elem, end = ' ')
    print()

def choose(curr_idx, num):
    # 초기 조건
    if curr_idx == m + 1:
        print_num()
        return

    for i in range(num + 1, n + 1):
        ans.append(i)
        choose(curr_idx + 1, i)
        ans.pop()


choose(1, 0)