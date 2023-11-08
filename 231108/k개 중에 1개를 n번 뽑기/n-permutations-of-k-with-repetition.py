def choose(n):
    if n == 0:
        print(' '.join(map(str, nums)))
        return

    for i in range(k):
        nums.append(i+1)
        choose(n-1)
        nums.pop()


k, n = tuple(map(int, input().split()))
nums = []

choose(n)