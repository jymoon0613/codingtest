# 국영수

## 나의 답안 ##

n = int(input())

array = []
for _ in range(n):
    name, a, b, c = input().split()
    array.append((name, int(a), int(b), int(c)))

array.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for x in array:
    print(x[0])

## 예시 답안 ##

n = int(input())

students = []
for _ in range(n):
    students.append(input().split())
    
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for students in students:
    print(students[0])
