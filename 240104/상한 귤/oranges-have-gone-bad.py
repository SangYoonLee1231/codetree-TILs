from collections import deque

n, k = tuple(map(int, input().split()))

start_box = [
    list(map(int, input().split()))
    for _ in range(n)
]

answer = [
    [-1] * n
    for _ in range(n)
]

q = deque()

drs = [0, 1, 0, -1]
dcs = [1, 0 , -1, 0]


def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n


def can_go(r, c):
    if not in_range(r, c):
        return False
    if not start_box[r][c]:
        return False
    if answer[r][c] != -1:
        return False
    return True


def bfs():
    while q:
        r, c, time = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc):
                q.append((nr, nc, time + 1))
                answer[nr][nc] = time + 1


# 시작점 구하기
# for i in range(n):
#     for j in range(n):
#         if start_box[i][j] == 2:
#             q.append((i, j, 0))
#             answer[i][j] = 0

# 시작점 구하기 개선 코드
s_pos = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if start_box[i][j] == 2
]

for elem in s_pos:
    r, c = elem
    q.append((r, c, 0))
    answer[r][c] = 0


# BFS 수행
bfs()

# 결과값 출력
for i in range(n):
    for j in range(n):
        if answer[i][j] == -1 and start_box[i][j] == 1:
            print(-2, end=" ")
        else:
            print(answer[i][j], end=" ")
    print()