# 1541: 잃어버린 괄호

lines = input().split('-')

lines_plus = [sum(list(map(int, l.split('+')))) for l in lines]

result = lines_plus[0]

for i in range(1, len(lines_plus)):
    result -= lines_plus[i]

print(result)