# 1464: 뒤집기 3

s = input()

for i in range(len(s)-1):
    if ord(s[i]) < ord(s[i+1]):
        temp = s[:i+1][::-1]
        temp = temp + s[i+1]
        s = temp[::-1] + s[i+2:]

result = s[::-1]

print(result)