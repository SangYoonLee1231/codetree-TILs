n = int(input())

# Step 1. 2진수 n -> 10진수 n
n_decimal = 0
lst_n = list(str(n))
lst_n_len = len(lst_n)

for i in range(len(lst_n)):
    n_decimal += int(lst_n[i]) * (2 ** (lst_n_len - i - 1))

# Step 2. 10진수 n * 17
n_decimal *= 17

# Step 3. 다시 2진수로 변경
ans_lst = []

while n_decimal > 0:
    ans_lst.append(n_decimal % 2)
    n_decimal //= 2

for elem in ans_lst[::-1]:
    print(elem, end="")
