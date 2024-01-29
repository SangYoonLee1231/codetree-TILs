n, m = tuple(map(int, input().split()))
lst = list(map(int, input().split()))
chosen = []
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
    
    for elem in lst:
        chosen.append(elem)
        backtrack(curr_num + 1)
        chosen.pop()


backtrack(0)
print(answer)