n = int(input())

# make_nums 함수: filled_nums자리만큼 숫자가 채워짐, 그 다음 자리부터 숫자를 채우는 함수
def make_nums(filled_nums):
    if filled_nums == n:
        return 1
    elif filled_nums > n:
        return 0
    
    count = 0

    for i in range(1, 5):
        count += make_nums(filled_nums + i)

    return count
    

print(make_nums(0))