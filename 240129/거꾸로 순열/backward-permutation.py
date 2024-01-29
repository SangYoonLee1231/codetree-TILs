n = int(input())

lst = []
visited = [False] * (n + 1)


def print_nums():
    for elem in lst:
        print(elem, end=' ')
    print()


def backtrack(curr_num):
    if curr_num == n:
        print_nums()
        return
    
    for i in range(n, 0, -1):
        if not visited[i]:
            lst.append(i)
            visited[i] = True
            backtrack(curr_num + 1)
            visited[i] = False
            lst.pop()


backtrack(0)