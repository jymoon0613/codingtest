# 실패율

## 나의 답안 ##

import json

n = int(input())

stages = input()
stages = json.loads(stages)

def solution(n, stages):

    result = []

    total = len(stages)

    for i in range(1, n+1):

        value = stages.count(i)

        if total == 0:
            fail = 0
        else:
            fail = value / total

        result.append((i, fail))
        total -= value

    result.sort(key=lambda x: x[1], reverse=True)

    result = [i[0] for i in result]

    print(result)

print(solution(n, stages))

## 예시 답안 ##

import json

N = int(input())

stages = input()
stages = json.loads(stages)

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