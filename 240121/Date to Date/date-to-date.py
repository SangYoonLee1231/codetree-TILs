m1, d1, m2, d2 = tuple(map(int, input().split()))

num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_days = 0
end_days = 0

for month in range(0, m1):
    start_days += num_of_days[month]
start_days += d1

for month in range(0, m2):
    end_days += num_of_days[month]
end_days += d2

print(end_days - start_days)