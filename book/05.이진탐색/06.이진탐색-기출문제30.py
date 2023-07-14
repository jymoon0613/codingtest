# 가사 검색

## 나의 답안 ##

words = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']
queries = ['fro??', '????o', 'fr???', 'fro???', 'pro?']

result = []
for q in queries:
    cnt = 0
    for w in words:
        if len(q) != len(w):
            continue
        
        ct = 0
        for (i, j) in zip(q,w):
            if (i == '?') or (i == j):
                ct += 1
        if ct == len(w):
            cnt += 1
    
    result.append(cnt)

print(result)

## 예시 답안 ##

from bisect import bisect_left, bisect_right

words = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']
queries = ['fro??', '????o', 'fr???', 'fro???', 'pro?']

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    
    return right_index - left_index

array = [[] for _ in range(10001)]

reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])
        
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()
        
    for q in queries:
        if q[0] != '?':
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
            
        else:
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
            
        answer.append(res)
    
    return answer

solution(words, queries)