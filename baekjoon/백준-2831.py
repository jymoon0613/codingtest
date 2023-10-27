# 2831: 댄스 파티

from collections import deque

n = int(input())

male = deque(sorted(list(map(int, input().split())), reverse=True))
female = deque(sorted(list(map(int, input().split()))))

result = 0
while male and female:

    m = male.popleft()
    if m > 0:
        if female[0] < 0:
            if abs(female[0]) > m:
                female.popleft()
                result += 1
            else:
                continue
        else:
            continue

    else:
        if female[0] > 0:
            if abs(m) > female[0]:
                female.popleft()
                result += 1
            else:
                continue
        else:
            female.popleft()
            male.appendleft(m)

print(result)