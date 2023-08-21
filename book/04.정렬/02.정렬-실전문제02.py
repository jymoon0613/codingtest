# 성적이 낮은 순서로 학생 출력하기

## 나의 답안 ##

n = int(input())

array = []
for _ in range(n):
    name, score = input().split()
    array.append((name, int(score)))

array.sort(key=lambda x: x[1])

for i in range(n):
    print(array[i][0], end=' ')

## 예시 답안 ##

n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))
    
array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0], end=' ')