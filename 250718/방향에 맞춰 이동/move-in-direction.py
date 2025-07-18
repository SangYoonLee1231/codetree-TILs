n = int(input())
moves = [
    list(input().split())
    for _ in range(n)
] # 숫자도 문자인 상태 -> 형변환 필요

dirConvert = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3,
}

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0


def moveOnce(move):
    global x, y

    dirEng, dist = move
    dist = int(dist)

    dr, dc = dxs[dirConvert[dirEng]], dys[dirConvert[dirEng]]
    x, y = x + dr * dist, y + dc * dist


for move in moves:
    moveOnce(move)

print(x, y)
