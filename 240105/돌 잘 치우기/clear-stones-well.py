from collections import deque

n, k, m = tuple(map(int, input().split()))

first_grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0] * n
    for _ in range(n)
]

start_points = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

q = deque()

erased_rocks = []

max_movable_squares = 0

drs = [1, 0, -1, 0]
dcs = [0, 1, 0, -1]



def initization():
    # visited 배열 초기화
    for i in range(n * n):
        visited[i // n][i % n] = 0
    
    # 시작 점들을 모두 큐에 추가
    for elem in start_points:
        r, c = elem
        r, c = r - 1, c - 1
        visited[r][c] = 1
        q.append((r, c))


def erase_rock(curr_rock_num, r, c):
    global max_movable_squares

    if m == 0:
        max_movable_squares = check_squares()
        return

    if curr_rock_num == m:
        # 초기화 작업
        initization()

        max_movable_squares = max(max_movable_squares, check_squares())
        return
    
    for i in range(r, n):
        for j in range(c, n):
            if r == i and c == j:
                continue
            if first_grid[i][j]:
                erased_rocks.append((i, j))
                erase_rock(curr_rock_num + 1, i, j)
                erased_rocks.pop()



def in_range(r, c):
    return r >= 0 and r < n and c >= 0 and c < n


def can_go(r, c):
    if not in_range(r, c):
        return False
    if visited[r][c]:
        return False
    return True


def check_squares():
    # 돌 제거
    for elem in erased_rocks:
        r, c = elem
        first_grid[r][c] = 0

    # print(first_grid)
    # print()

    # 칸 세기

    cnt = len(start_points)

    while q:
        r, c = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if can_go(nr, nc) and first_grid[nr][nc] == 0:
                cnt += 1
                q.append((nr, nc))
                visited[nr][nc] = 1

    # 돌 원상복구
    for elem in erased_rocks:
        r, c = elem
        first_grid[r][c] = 1
        
    return cnt
                

flag = False

for i in range(n * n):
    if first_grid[i // n][i % n]:
        flag = True

        erased_rocks.append((i // n, i % n))
        erase_rock(1, i // n, i % n)
        erased_rocks.pop()

        break

print(max_movable_squares if flag else n * n)