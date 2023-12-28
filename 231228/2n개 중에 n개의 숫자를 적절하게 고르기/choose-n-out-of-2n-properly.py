import sys

n = int(input())
lst = list(map(int, input().split()))
visited = [False] * (2*n)
total_sum = 0
answer = sys.maxsize

for elem in lst:
    total_sum += elem


def select(selected_num, idx, group_sum):
    global answer

    if selected_num == n:
        answer = min(answer, abs(total_sum - 2 * group_sum))
    
    for i in range(idx, 2*n):
        if visited[i] == True:
            continue

        visited[i] = True
        select(selected_num + 1, i, group_sum + lst[i])
        visited[i] = False


select(0, 0, 0)
print(answer)