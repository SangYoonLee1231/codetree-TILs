n = int(input())

answer = 0


def beautiful_num(curr_idx):
    global answer

    if curr_idx == n:
        answer += 1
        return
    elif curr_idx > n:
        return
    
    for i in range(1, 5):
        beautiful_num(curr_idx + i)


beautiful_num(0)
print(answer)