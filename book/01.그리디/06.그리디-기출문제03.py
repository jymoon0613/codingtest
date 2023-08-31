# 문자열 뒤집기

## 나의 답안 ##

array = list(map(int, input()))

num0 = 0
num1 = 0
for i in range(len(array)-1):
    if array[i] == 0 and array[i+1] == 1:
        num0 += 1
    if array[i] == 1 and array[i+1] == 0:
        num1 += 1

if array[-1] == 0:
    num0 += 1
else:
    num1 += 1

print(min(num0, num1))

## 예시 답안 ##

data = input()

count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))