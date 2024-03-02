a, b = tuple(map(int, input().split()))

answer = 0
quo, rem = -1, -1
rem_lst = [0] * 10

while a > 1:
    quo = a // b
    rem = a % b

    rem_lst[rem] += 1
    a = quo

for elem in rem_lst:
    answer += (elem ** 2)

print(answer)