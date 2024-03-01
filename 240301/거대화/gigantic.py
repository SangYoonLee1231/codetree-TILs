n, k = tuple(map(int, input().split()))

num_lst = list(input())
length = len(num_lst)
answer = 0


def check_biggest_num():
    global answer
    
    temp_lst = []

    for elem in num_lst:
        if not elem:
            continue
        temp_lst.append(elem)

    temp_num = int(''.join(map(str, temp_lst)))
    answer = max(answer, temp_num)


def backtrack(curr_idx, erased_count):
    if erased_count == k:
        check_biggest_num()

    for i in range(curr_idx + 1, length):
        temp = num_lst[i]
        num_lst[i] = 0
        backtrack(i, erased_count + 1)
        num_lst[i] = temp


backtrack(-1, 0)
print(answer)