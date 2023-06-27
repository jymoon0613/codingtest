# 숫자 카드 게임

N, M = list(map(int, input().split()))

array = [list(map(int, input().split())) for _ in range(N)]

res = -1
ind_row = None

for i in range(N):
    arr = array[i]
    
    mini = min(arr)
    
    if mini > res:
        res = mini
        ind_row = i
        
print(res)