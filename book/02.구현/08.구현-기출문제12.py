# 기둥과 보 설치

## 나의 답안 ## 

import json

n = int(input())

build_frame = input()

build_frame = json.loads(build_frame)

def check(frames):

    for frame in frames:

        x, y, a = frame

        if a == 0:

            if y == 0 or (x, y-1, 0) in frames or (x-1, y, 1) in frames or (x+1, y, 1) in frames:

                continue
            
            else:

                return False
        
        else:
            if ((x-1, y, 1) in frames and (x+1, y, 1) in frames) or (x, y-1, 0) in frames or (x+1, y-1, 0) in frames:

                continue
            
            else:

                return False
            
    return True

def solution(build_frame):

    result = []
    for frame in build_frame:
        
        x, y, a, b = frame

        if b == 0:
            result.remove((x, y, a))
            ok = check(result)

            if not ok:
                result.append((x, y, a))

        else:
            result.append((x, y, a))
            ok = check(result)

            if not ok:
                result.remove((x, y, a))
    result.sort()
    print(result)

solution(build_frame)

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


