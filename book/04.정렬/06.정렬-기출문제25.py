# 실패율

## 나의 답안 ##

N = int(input())

stages = list(map(int, input().split()))

stages.sort()

res = []
for i in range(1, N+1):
    u = 0
    d = 0
    for j in stages:
        if i == j:
            u += 1
        if i <= j:
            d += 1
            
    res.append((u/d, i))

res.sort(key=lambda x: x[0], reverse=True)

l = []
for r in res:
    l.append(r[1])
    
print(l)

## 예시 답안 ##

N = int(input())

stages = list(map(int, input().split()))

def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1, N+1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        answer.append((i, fail))
        length -= count
    
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
    answer = [i[0] for i in answer]
    
    return answer

print(solution(N, stages))