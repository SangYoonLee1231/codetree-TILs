n = int(input())
input_lst = list(map(int, input().split()))

answer_lst = []

for elem in input_lst:
    if elem % 2 == 0:
        answer_lst.append(elem)

len_of_answers = len(answer_lst)

for i in range(len_of_answers - 1, -1, -1):
    print(answer_lst[i], end=" ")