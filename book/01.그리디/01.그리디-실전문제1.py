# 큰 수의 법칙

N, M, K = list(map(int, input().split()))

array = list(map(int, input().split()))

array_sorted = sorted(array, reverse=True)

res = 0
cnt = 0

while True:
    
    num1 = array_sorted[0]
    num2 = array_sorted[1]
    
    for i in range(K):
        
        if cnt == M:
            break
        
        res += num1
        
        cnt += 1
            
    if cnt == M:
        break
        
    res += num2
        
    cnt += 1
            
print(res)