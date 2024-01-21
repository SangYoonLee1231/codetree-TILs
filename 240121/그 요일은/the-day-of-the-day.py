m1, d1, m2, d2 = tuple(map(int, input().split()))
target_day = input()

week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
num_of_days = [0, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_day, end_day = 0, 0

for month in range(1, m1):
    start_day += num_of_days[month]
start_day += d1

for month in range(1, m2):
    end_day += num_of_days[month]
end_day += d2

# Part 1
gap = end_day - start_day + 1
answer = gap // 7

# Part 2
if (gap % 7) > week.index(target_day):
    answer += 1

print(answer)