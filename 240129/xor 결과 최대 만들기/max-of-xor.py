n, m = tuple(map(int, input().split()))
lst = list(map(int, input().split()))
chosen = []
visited = [False] * n
answer = 0


def calc_xor():
    result = chosen[0]
    for i in range(1, len(chosen)):
        result = result ^ chosen[i]
    
    return result


def backtrack(curr_num):
    global answer

    if curr_num == m:
        answer = max(answer, calc_xor())
        return
    
    for idx, elem in enumerate(lst):
        if not visited[idx]:
            chosen.append(elem)
            visited[idx] = True
            backtrack(curr_num + 1)
            visited[idx] = False
            chosen.pop()


backtrack(0)
print(answer)