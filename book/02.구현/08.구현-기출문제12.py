# 기둥과 보 설치

## 나의 답안 ## 

import json

def check(order, accum):
    x, y, a, _ = order
    if a == 0:
        if (y == 0) or ([x-1, y, 1, 1] in accum) or ([x, y-1, 0, 1] in accum):
            return True
        
        else:
            return False
        
    else:
        if ([x, y-1, 0, 1] in accum) or ([x+1, y-1, 0, 1] in accum) or (([x-1, y, 1, 1] in accum) and ([x+1, y, 1, 1] in accum)):
            return True
        
        else:
            return False

n = int(input())

build_frame = input()

build_frame = json.loads(build_frame)

accum = []
res = []
for build in build_frame:
    
    b = build[-1]
    
    if b == 0:
        exists = []
        for exist in accum:
            x, y, a, _ = exist
            if (x == build[0]) and (y == build[1]) and (a == build[2]):
                continue
            else:
                exists.append(exist)
        
        accum_new = []
        res_new = []
        
        for exist in exists:
            c = check(exist, exists)
            if c == False:
                break
            else:
                accum_new.append(exist)
                res_new.append(exist[:-1])
        
        if c != False:
            accum = accum_new
            res = res_new
            
        else:
            continue
            
    else:
        
        c = check(build, accum)
    
        if c == True:
            accum.append(build)
            res.append(build[:-1])

        else:
            continue
            
res.sort(key=lambda x: (x[0], x[1], x[2]))
print(res)

## 예시 답안 ##

import json

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue

            return False
        
        elif stuff == 1:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue

            return False
        
    return True
        
def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])

        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])

    return sorted(answer)

n = int(input())

build_frame = input()

build_frame = json.loads(build_frame)

print(solution(n, build_frame))


