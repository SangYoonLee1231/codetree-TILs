n = int(input())
answer = []
visited = [False] * (n + 1)


def print_answer():
    for elem in answer:
        print(elem, end=' ')
    print()


def choose(curr_n):
    if curr_n == n + 1:
        print_answer()
        return
    
    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = True
        answer.append(i)
        choose(curr_n + 1)
        answer.pop()
        visited[i] = False


choose(1)