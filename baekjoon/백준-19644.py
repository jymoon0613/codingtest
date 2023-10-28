# 19644: 좀비 떼가 기관총 진지에도 오다니

import sys
from collections import deque

input = sys.stdin.readline

l = int(input())
ml, mk = map(int, input().split())
ammo = int(input())

zombie = [0] + [int(input()) for _ in range(l)]

possible = True
attack = [0]
for i in range(1, l+1):

    d = max(i-ml, 0)

    damage = attack[i-1] - attack[d]

    if zombie[i] <= damage + mk:
        attack.append(attack[i-1] + mk)
    else:
        if ammo > 0:
            ammo -= 1
            attack.append(attack[i-1])
        else:
            possible = False
            break

if possible:
    print('YES')
else:
    print('NO')