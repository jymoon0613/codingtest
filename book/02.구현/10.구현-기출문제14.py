# 외벽 점검

## 나의 답안 ##

import json
from itertools import permutations

n = int(input())

weak = input()
weak = json.loads(weak)

dist = input()
dist = json.loads(dist)

def solution(n, weak, dist):

    length = len(weak)

    for i in range(len(weak)):

        weak.append(weak[i] + n)

    result = len(dist) + 1
    for start in range(length):

        candidates = permutations(dist, len(dist))

        for candidate in candidates:
            
            cnt = 1

            position = weak[start] + candidate[cnt-1]

            for i in range(start, start + length):
                
                if weak[i] > position:

                    cnt += 1

                    if cnt >= len(candidate):
                        
                        break

                    position = weak[i] + candidate[cnt-1]

            result = min(result, cnt)

    if result > len(dist):
        print(-1)
    else:
        print(result)

solution(n, weak, dist)

## 예시 답안 ##

import json
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
        
    answer = len(dist) + 1
    
    for start in range(length):
        for friends in list(permutations(dist, len(dist))):
            count = 1
            position = weak[start] + friends[count-1]
            
            for index in range(start, start+length):
                
                if position < weak[index]:
                    count += 1
                    if count > len(dist):
                        break
                    position = weak[index] + friends[count-1]
                    
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    
    return answer

n = int(input())

weak = input()
weak = json.loads(weak)

dist = input()
dist = json.loads(dist)

print(solution(n, weak, dist))