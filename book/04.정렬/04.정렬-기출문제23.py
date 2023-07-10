# 국영수

## 나의 답안 ##

N = int(input())

array = []
for i in range(N):
    input_data = input().split()
    array.append((input_data[0], -int(input_data[1]), int(input_data[2]), -int(input_data[3])))
    
array.sort(key=lambda x: (x[1], x[2], x[3], [ord(i) for i in x[0]]))

for i in range(N):
    print(array[i][0])

## 예시 답안 ##

n = int(input())

students = []
for _ in range(n):
    students.append(input().split())
    
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for students in students:
    print(students[0])
