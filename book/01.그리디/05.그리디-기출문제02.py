# 곱하기 혹은 더하기

nums = list(input())

res = 0

for num in nums:
    
    num = int(num)
    
    if (res <= 1) or (num <= 1):
        res += num
        
    else:
        res *= num

print(res)