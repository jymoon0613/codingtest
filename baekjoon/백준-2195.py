# 2195: 문자열 복사

s = input()
p = input()

candiate = []
for step in range(1, len(s)+1):
    for j in range(len(s)-step+1):
        candiate.append(s[j:j+step])

candiate = set(candiate)

result = 0
i = 0
now = ''
while i < len(p):
    now += p[i]

    if now in candiate:
        i += 1
        continue
    else:
        now = ''
        result += 1
        continue

print(result+1)