# 1543: 문서 검색

text = input()
target = input()

result = 0
cnt = 0
for i in range(len(text)-len(target)+1):
    t = text[i:i+len(target)]
    if t == target:
        if cnt <= 0:
            result += 1
            cnt = len(target)
    cnt -= 1

print(result)