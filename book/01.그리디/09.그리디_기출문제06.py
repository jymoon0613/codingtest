# 무지의 먹방 라이브

## 나의 답안 ##

food_times = list(map(int, input().split()))
k = int(input())

def solution(food_times, k):

    cnt = 0
    head = 0
    zero_count = 0

    while True:
        
        head %= len(food_times)

        if food_times[head] == 0:
            zero_count += 1
            head += 1

            if zero_count == len(food_times):
                break

            continue

        food_times[head] -= 1
        head += 1
        cnt += 1
        zero_count = 0

        if cnt == k or zero_count == len(food_times):
            break

    if zero_count == len(food_times):
        return -1
    else:
        return head % len(food_times) + 1

print(solution(food_times, k))

## 예시 답안 ##

import heapq

food_times = list(map(int, input().split()))
k = int(input())

def solution(food_times, k):

    if sum(food_times) <= k:

        return -1

    q = []
    for i in range(len(food_times)):

        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0
    previous = 0

    length = len(food_times)

    while sum_value + ((q[0][0] - previous) * length) <= k:
        
        now = heapq.heappop(q)[0]

        sum_value += (now - previous) * length

        length -= 1

        previous = now

    result = sorted(q, key=lambda x: x[1])

    return result[(k-sum_value) % length][1]

print(solution(food_times, k))