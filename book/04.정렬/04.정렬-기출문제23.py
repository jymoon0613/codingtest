# 국영수

## 나의 답안 ##

n = int(input())

array = []
for _ in range(n):
    name, kor, eng, mat = input().split()
    array.append((-int(kor), int(eng), -int(mat), name))

array.sort()

for i in range(n):
    print(array[i][-1])

## 예시 답안 ##

n = int(input())

students = []
for _ in range(n):
    students.append(input().split())
    
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for students in students:
    print(students[0])
