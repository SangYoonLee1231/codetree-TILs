# Sol 1) 인접 리스트로 해결
n, m = tuple(map(int, input().split()))
graph = [[] for _ in range (n + 1)]
visited = [False for _ in range (n + 1)]
answer = -1

for _ in range(m):
    start, end = tuple(map(int, input().split()))
    graph[start].append(end)
    graph[end].append(start)


# DFS 방식으로 그래프를 탐색하는 함수
def search(curr_v):
    for elem in graph[curr_v]:
        if not visited[elem]:
            visited[elem] = True
            search(elem)
            

visited[1] = True
search(1)

for elem in visited:
    if elem:  answer += 1

print(answer)


# Sol 2) 인접 행렬로 해결
n, m = tuple(map(int, input().split()))

graph = [
    [0] * (n + 1)
    for _ in range(n + 1)
]

visited = [False for _ in range(n + 1)]

answer = -1

for _ in range(m):
    start, end = tuple(map(int, input().split()))
    graph[start][end] = 1
    graph[end][start] = 1


def search(curr_v):
    for idx, elem in enumerate(graph[curr_v]):
        if not visited[idx] and elem:
            visited[idx] = True
            search(idx)


visited[1] = True
search(1)

for elem in visited:
    if elem:   answer += 1

print(answer)