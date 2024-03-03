n = int(input())
lst = list(map(int, input().split()))

count = 0

for i, elem in enumerate(lst):
    if elem == 2:
        count += 1
    if count == 3:
        print(i + 1)
        break