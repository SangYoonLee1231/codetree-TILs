k, n = tuple(map(int, input().split()))
num = []

def print_num():
    for elem in num:
        print(elem, end = ' ')
    print()

def choose(curr_num):
    if curr_num == n + 1:
        if curr_num >= 4 and num[n-1] == num[n-2] and num[n-2] == num[n-3]:
            return
        print_num()
        return
    
    for i in range(1, k+1):
        num.append(i)
        choose(curr_num + 1)
        num.pop()

choose(1)