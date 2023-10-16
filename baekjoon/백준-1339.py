# 1339: 단어 수학

n = int(input())

words = []
word_list = []
counts = []

data_list = []
for i in range(n):
    data = input()
    data_list.append(data)
    power = len(data) - 1
    for j in range(len(data)):
        exist = False
        for k in range(len(word_list)):
            if data[j] == word_list[k]:
                counts[k] += 10 ** power
                power -= 1
                exist = True
                break
        if not exist:
            word_list.append(data[j])
            counts.append(10 ** power)
            power -= 1

word_sort = [word[1] for word in sorted([(count, num) for count, num in zip(counts, word_list)], reverse=True)]

result = 0
for data in data_list:
    num = ''
    for i in range(len(data)):
        for j in range(len(word_sort)):
            if data[i] == word_sort[j]:
                num += str(9-j)
    result += int(num)

print(result)