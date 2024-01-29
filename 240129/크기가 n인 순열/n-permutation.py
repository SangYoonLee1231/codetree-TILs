n = int(input())
visited = [False] * (n + 1)
lst = []


def print_lst():
    for elem in lst:
        print(elem , end=' ')
    print()


def choose(curr_idx):
    if curr_idx == n:
        print_lst()
        return
    
    for i in range(1, n + 1):
        if not visited[i]:
            lst.append(i)
            visited[i] = True
            choose(curr_idx + 1)
            visited[i] = False
            lst.pop()


choose(0)