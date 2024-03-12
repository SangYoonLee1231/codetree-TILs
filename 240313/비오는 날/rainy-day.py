n = int(input())

input_lst = [
    list(input().split())
    for _ in range(n)
]

rain_lst = []

# months_common_year = [
#     31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
# ]

# months_leap_year = [
#     31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
# ]

# Rain 요소만 뽑아 담은 rain_lst 구성
for elem in input_lst:
    if elem[2] == 'Rain':
        rain_lst.append(elem)

rain_lst_len = len(rain_lst)

# 날짜 정렬을 위한 입력값 리스트 수정
# (1달이 모두 31일이라 가정 => 1년은 372일)
for i in range(rain_lst_len):
    year, month, day = rain_lst[i][0].split('-')
    time = year * 372 + month * 31 + day
    rain_lst[i].append(day)

sorted(rain_lst, key=lambda x:x[3])

rain_lst[0].pop()

for elem in rain_lst[0]:
    print(elem, end=' ')