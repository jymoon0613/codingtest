# 괄호 변환

## 나의 답안 ##

from collections import deque

p = input()

def is_balance(p):
    
    cnt0 = 0
    cnt1 = 0

    for s in p:
        if s == '(':
            cnt0 += 1
        else:
            cnt1 += 1

    if cnt0 == cnt1:
        return True
    else:
        return False
    
def is_correct(p):

    if not is_balance(p):
    
        return False

    cnt0 = 0
    cnt1 = 0

    for s in p:

        if s == '(':
            cnt0 += 1
        else:
            cnt1 += 1

        if (cnt0 - cnt1) < 0:

            return False
        
    return True

def solution(p):

    result = ''

    if len(p) == 0:
        
        return result
    
    for i in range(1, len(p)+1):

        u = p[:i]
        v = p[i:]

        if is_balance(u):

            break

    if is_correct(u):

        result = u + solution(v)
    
    else:

        result = '('
        result += solution(v)
        result += ')'
        u = list(u[1:-1])
        for s in u:
            if s =='(':
                result += ')'
            else:
                result += '('

    return result

print(solution(p))

## 예시 답안 ##

def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i
        
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
            
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index+1]
    v = p[index+1:]
    
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
                
        answer += "".join(u)
        
    return answer

p = input()

print(solution(p))