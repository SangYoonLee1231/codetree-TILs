n = int(input())

block_lst = [
    int(input())
    for _ in range(n)
]

explode_lst = []
for _ in range(2):
    explode_lst.append(tuple(map(int, input().split())))


end_of_array = n
temp_lst = [0] * n

for i in range(2):
    end_of_temp_array = 0

    for j in range(0, end_of_array):
        if j >= (explode_lst[i][0] - 1) and j <= (explode_lst[i][1] - 1):
            continue
        
        temp_lst[end_of_temp_array] = block_lst[j]
        end_of_temp_array += 1
        
    end_of_array = end_of_temp_array

    for j in range(0, end_of_array):
        block_lst[j] = temp_lst[j]


print(end_of_array)
for i in range(end_of_array):
    print(block_lst[i])