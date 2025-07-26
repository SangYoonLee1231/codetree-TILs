n = int(input())
words = [input() for _ in range(n)]

# Please write your code here.
words_dict = {}

for i, elem in enumerate(words):
    if elem not in words_dict:
        words_dict[elem] = 1
    else:
        words_dict[elem] += 1

print(max(words_dict.values()))