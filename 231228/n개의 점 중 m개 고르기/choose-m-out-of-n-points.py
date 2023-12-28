import sys

n, m = tuple(map(int, input().split()))
lst = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [False] * n
answer = sys.maxsize

selected_dot = []

def calc_dist(x1, y1, x2, y2):
    return (x1 - x2)**2 + (y1 - y2)**2


def find_shortest(selected_dot):
    global answer

    length = len(selected_dot)
    
    for i in range(length):
        for j in range(i + 1, length):
            answer = min(answer, calc_dist(selected_dot[i][0], selected_dot[i][1], selected_dot[j][0], selected_dot[j][1]))


def choose_dot(selected_num):
    if selected_num == m:
        find_shortest(selected_dot)
    
    for i in range(len(lst)):
        if visited[i] == True:
            continue
            
        visited[i] = True
        selected_dot.append(lst[i])
        choose_dot(selected_num + 1)
        selected_dot.pop()
        visited[i] = False


choose_dot(0)
print(answer)