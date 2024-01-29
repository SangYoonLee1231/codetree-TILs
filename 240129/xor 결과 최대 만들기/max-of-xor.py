n, m = tuple(map(int, input().split()))
lst = list(map(int, input().split()))
chosen = []
answer = 0


def calc_xor():
    result = chosen[0]
    for i in range(1, m):
        result = result ^ chosen[i]

    return result


def backtrack(curr_num, last_idx):
    global answer

    if curr_num == m:
        answer = max(answer, calc_xor())
        return
    
    for idx in range(last_idx + 1, len(lst)):
        chosen.append(lst[idx])
        backtrack(curr_num + 1, idx)
        chosen.pop()


backtrack(0, -1)
print(answer)