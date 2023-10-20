# 4949: 균형잡힌 세상

from collections import deque

while True:
    line = input()
    if line == '.':
        break

    check = True
    q = deque()
    for word in line:
        if word == '(' or word == '[':
            q.append(word)
        if word == ')' or word == ']':
            if len(q) == 0:
                check = False
                break
            w = q.pop()
            if word == ')' and w == '[':
                check = False
                break
            if word == ']' and w == '(':
                check = False
                break
    
    if len(q) != 0:
        check = False
    
    if not check:
        print('no')
    else:
        print('yes')