a, b, c = tuple(map(int, input().split()))

start_time = 11 * 60 + 11


def find_times():
    if a < 11:
        return -1
    
    end_time = (a - 11) * 1440 + b * 60 + c
    return end_time - start_time

answer = find_times()
print(answer if answer else -1)