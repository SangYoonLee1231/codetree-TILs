n, m, k = tuple(map(int, input().split()))
n_lst = list(map(int, input().split()))
players = [1] * k
max_score = 0

def check_passed_goal():
    score = 0

    for elem in players:
        if elem >= m:
            score += 1

    return score
        

def backtrack(curr_turn):
    global max_score

    if curr_turn == n:
        score = check_passed_goal()
        max_score = max(max_score, score)
        return
    
    for idx in range(k):
        players[idx] += n_lst[curr_turn]
        backtrack(curr_turn + 1)
        players[idx] -= n_lst[curr_turn]


backtrack(0)
print(max_score)