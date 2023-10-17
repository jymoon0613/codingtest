# 2212: 센서

n = int(input())

k = int(input())

position = list(map(int, input().split()))

position.sort()

def solution():

    if k >= n:
        return 0
    
    dist = []
    for i in range(1, n):
        dist.append(position[i] - position[i-1])

    dist.sort(reverse=True)
    for _ in range(k-1):
        dist.pop(0)

    return sum(dist)

print(solution())