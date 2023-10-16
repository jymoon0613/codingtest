# 1744: 수 묶기

n = int(input())

data_p = []
data_m = []
n_zero = 0
for _ in range(n):
    num = int(input())
    if num > 0:
        data_p.append(num)
    elif num < 0:
        data_m.append(num)
    else:
        n_zero += 1

data_p.sort(reverse=True)
data_m.sort()

data_bind = []
while data_p:
    num1 = data_p.pop(0)
    if len(data_p) == 0:
        data_bind.append(num1)
        break
    
    num2 = data_p.pop(0)

    if num1 == 1 or num2 == 1:
        data_bind.append(num1)
        data_bind.append(num2)
    else:
        data_bind.append(num1 * num2)

while data_m:
    num1 = data_m.pop(0)
    if len(data_m) == 0:
        if n_zero == 0:
            data_bind.append(num1)
            break
        else:
            break

    num2 = data_m.pop(0)

    data_bind.append(num1 * num2)

result = sum(data_bind)
print(result)