# k, n = tuple(map(int, input().split()))
# num = []

# def print_num():
#     for elem in num:
#         print(elem, end = ' ')
#     print()

# def condition():
#     for i in range(n-2):
#         if num[i] == num[i+1] and num[i+1] == num[i+2]:
#             return True
#     return False

# def choose(curr_num):
#     if curr_num == n + 1:
#         if curr_num >= 4 and condition():
#             return
#         print_num()
#         return
    
#     for i in range(1, k+1):
#         num.append(i)
#         choose(curr_num + 1)
#         num.pop()

# choose(1)

k, n = tuple(map(int, input().split()))
num = []

def print_num():
    for elem in num:
        print(elem, end = ' ')
    print()

# curr_num의 위치에 숫자를 선택하는 함수
def choose(curr_num):
    if curr_num == n + 1:
        print_num()
        return
    
    for i in range(1, k+1):
        if curr_num >= 4 and num[-1] == num[-2] and num[-2] == num[-3]:
            continue
        num.append(i)
        choose(curr_num + 1)
        num.pop()

choose(1)