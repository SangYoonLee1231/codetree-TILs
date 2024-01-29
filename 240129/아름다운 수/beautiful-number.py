n = int(input())
# string = ''
answer = 0


def print_str():
    print()


def backtrack(curr_len):
    global answer

    if curr_len == n:
        answer += 1
        return

    if curr_len > n:
        return

    for i in range(1, 5):
        # string += (str(i) * i)
        backtrack(curr_len + i)



backtrack(0)
print(answer)

# string = ''
# string += str(3) * 3
# print(string)