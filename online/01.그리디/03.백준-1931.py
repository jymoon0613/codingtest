# 1931: 회의실 배정

# 참고: https://suri78.tistory.com/26

n = int(input())

array = []
for _ in range(n):
    s, e = map(int, input().split())
    array.append((s, e))

array.sort(key=lambda x: (x[1], x[0]))

result = 1
end_time = array[0][1]
for i in range(1, n):
    if array[i][0] >= end_time:
        result += 1
        end_time = array[i][1]

print(result)