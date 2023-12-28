n = int(input())
lst = []
visited = [False] * (n + 1)


def print_num():
    for elem in lst:
        print(elem, end = ' ')
    print()


# curr_num 인덱스를 채우기 위한 번호를 고르는 함수
def choose(curr_num):
    if curr_num == n:
        print_num()
        return
    
    for i in range(n, 0, -1):
        if visited[i]:
            continue
        
        visited[i] = True
        lst.append(i)
        choose(curr_num + 1)
        lst.pop()
        visited[i] = False


choose(0)