n = int(input())
count = 0

# make_nums 함수: filled_nums자리만큼 숫자가 채워짐, 그 다음 자리부터 숫자를 채우는 함수
def make_nums(filled_nums):
    global count
    
    if filled_nums == n:
        count += 1
        return
    elif filled_nums > n:
        return
    
    for i in range(1, 5):
        make_nums(filled_nums + i)
    

make_nums(0)
print(count)