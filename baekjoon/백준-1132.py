# 1132: 합

n = int(input())

num = [[0, chr(i+65)] for i in range(10)]
nonzero = [0] * 10
for _ in range(n):
    word = input()
    nonzero[ord(word[0])-65] = 1
    for i in range(len(word)):
        num[ord(word[i])-65][0] += 10 ** (len(word)-i-1)

num.sort(reverse=True)
if num[9][0] != 0:
    for i in range(9,-1,-1):
        if nonzero[ord(num[i][1])-65] == 0:
            temp = list(num[i])
            num.remove(temp)
            num.append(temp)
            break

result = 0
for i in range(10):
    result += num[i][0] * (9-i)

print(result)