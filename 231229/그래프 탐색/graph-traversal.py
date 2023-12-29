n, m = tuple(map(int, input().split()))
lst = [[] for _ in range (n + 1)]
visited = [False for _ in range (n + 1)]
answer = -1

for _ in range(m):
    start, end = tuple(map(int, input().split()))
    lst[start].append(end)
    lst[end].append(start)

# print(lst)


# DFS 방식으로 그래프를 탐색하는 함수
def search(curr_v):
    for elem in lst[curr_v]:
        if not visited[elem]:
            visited[elem] = True
            search(elem)
            

visited[1] = True
search(1)

for elem in visited:
    if elem:  answer += 1

print(answer)