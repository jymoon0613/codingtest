# 17609: 회문

n = int(input())

array = [input() for _ in range(n)]

for string in array:
    i = 0
    j = len(string) - 1
    result = 0
    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            if i + 1 <= j:
                temp = string[:i] + string[i+1:]
                if temp == temp[::-1]:
                    result = 1
                    break
            if i <= j - 1:
                temp = string[:j] + string[j+1:]
                if temp == temp[::-1]:
                    result = 1
                    break
            result = 2
            break
    
    print(result)