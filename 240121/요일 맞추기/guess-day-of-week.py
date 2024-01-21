m1, d1, m2, d2 = tuple(map(int, input().split()))

week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
nums_of_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

start_day, end_day = 0, 0

for month in range(1, m1):
    start_day += nums_of_day[month]
start_day += d1

for month in range(1, m2):
    end_day += nums_of_day[month]
end_day += d2


def check_day_of_the_week():
    gap = end_day - start_day

    return week[gap % 7]


print(check_day_of_the_week())