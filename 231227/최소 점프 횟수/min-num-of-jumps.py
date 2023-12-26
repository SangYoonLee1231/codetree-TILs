import sys

n = int(input())
lst = list(map(int, input().split()))
ans = sys.maxsize

# idx에서 n으로 가기 위해 가능한 점프 경우를 탐색하는 함수 (cnt=점프횟수)
def find_min_jump(idx, n, cnt):
    global ans
    
    # 초기 조건
    if idx == n:
        ans = min(ans, cnt)
        return
    elif idx > n:
        return

    for i in range(1, lst[idx]+1):
        find_min_jump(idx+i, n, cnt+1)


find_min_jump(0, n-1, 0)
print(ans if (ans != sys.maxsize) else -1)