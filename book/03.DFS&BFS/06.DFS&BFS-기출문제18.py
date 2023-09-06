# 괄호 변환

## 나의 답안 ##

def is_balance(string):

    cnt = 0
    for s in string:
        if s == '(':
            cnt += 1
        else:
            cnt -= 1

    if cnt != 0:
        return False
    else:
        return True
    
def is_proper(string):

    cnt = 0
    for s in string:
        if s == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0:
            return False
        
    return True

def solution(string):

    result = ''

    if len(string) == 0:

        return result
    
    for i in range(1, len(string)+1):
        u = string[:i]
        v = string[i:]

        if is_balance(u): break

    if is_proper(u): 
        result = u + solution(v)

    else:
        result = ''
        result += '('
        result += solution(v)
        result += ')'
        for uu in u[1:-1]:
            if uu == '(':
                result += ')'
            else:
                result += '('

    return result

p = input()
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