n, r, c = map(int, input().split())
grid = [[0] * (n) for _ in range(n)]

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# Please write your code here.
drs, dcs = [-1, 1, 0, 0], [0, 0, 1, -1]
r, c = r - 1, c - 1


def move():
    global r, c

    for i in range(4):
        dr, dc = drs[i], dcs[i]
        nr, nc = r + dr, c + dc

        if (inRange(nr, nc) and grid[r][c] < grid[nr][nc]):
            r, c = nr, nc
            return True
    
    return False



def inRange(r, c):
    return r >= 0 and r < n and c >= 0 and c < n


def solution():
    while True:
        print(grid[r][c], end=' ')

        moved = move()

        if not moved:
            break


# t번만큼 move -> move을 t회 반복
solution()