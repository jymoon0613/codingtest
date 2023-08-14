# 문자열 뒤집기

## 나의 답안 ##

nums = input()

cnt_0 = 0
cnt_1 = 0

for i in range(len(nums)-1):
    if nums[i] == '0' and (nums[i] != nums[i+1]):
        cnt_0 += 1
    elif nums[i] == '1' and (nums[i] != nums[i+1]):
        cnt_1 += 1
    else: 
        continue

if nums[-1] == '1':
    cnt_1 += 1
else:
    cnt_0 += 1

print(min(cnt_0, cnt_1))

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