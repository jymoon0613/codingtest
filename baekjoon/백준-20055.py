# 20055: 컨베이어 벨트 위의 로봇

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

a = deque(list(map(int, input().split())))

robot = []
def move_belt(a, robot):

    x = a.pop()
    a.appendleft(x)

    new_robot = [(x+1) % (2*n) for x in robot if (x+1) != (n-1)]

    return a, new_robot

def move_robot(a, robot):

    new_robot = []
    for i in range(len(robot)):
        x = robot[i]
        nx = (x+1) % (2*n)
        if nx not in new_robot and a[nx] >= 1:
            a[nx] -= 1
            if nx != (n-1):
                new_robot.append(nx)
        else:
            new_robot.append(x)

    return a, new_robot

def add_robot(a, robot):

    if a[0] > 0 and 0 not in robot:
        robot.append(0)
        a[0] -= 1

    return a, robot

def check(a):

    cnt = list(a).count(0)

    if cnt >= k: return False
    else: return True
        
result = 0 
while True:

    result += 1

    a, robot = move_belt(a, robot)

    a, robot = move_robot(a, robot)

    a, robot = add_robot(a, robot)

    possible = check(a)

    if not possible:
        break

print(result)