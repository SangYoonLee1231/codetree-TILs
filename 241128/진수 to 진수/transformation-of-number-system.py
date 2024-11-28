a, b = tuple(map(int, input().split()))
n = int(input())

# Step 1. a진수 n을 10진수로 변환
num = 0
a_lst = list(str(n))

for elem in a_lst:
    num = num * a + int(elem)

# Step 2. 10진수 n을 b진수로 변환
ans_lst = []

while num > 0:
    ans_lst.append(num % b)
    num //= b

print(''.join(map(str, ans_lst)))
