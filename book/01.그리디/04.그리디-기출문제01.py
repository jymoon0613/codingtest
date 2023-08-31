# 모험가 길드

## 나의 답안 ##

n = int(input())

array = list(map(int, input().split()))

array.sort()

cnt = 0
result = 0
for i in range(n):
    cnt += 1
    if cnt == array[i]:
        result += 1
        cnt = 0
        
print(result)

## 예시 답안 ##

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0
    
print(result)