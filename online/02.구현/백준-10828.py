# 10828: 스택

import sys

input = sys.stdin.readline

n = int(input())

array = []
for _ in range(n):
    command = list(input().split())

    if command[0] == 'push':
        array.append(int(command[1]))

    elif command[0] == 'pop':
        if len(array) == 0:
            print(-1)
        else:
            print(array.pop())

    elif command[0] == 'size':
        print(len(array))

    elif command[0] == 'empty':
        if len(array) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(array) == 0:
            print(-1)
        else:
            print(array[-1])