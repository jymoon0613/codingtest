# 14500: 테크로미노

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

array_pad = [[0] * (m + 6) for _ in range(n + 6)]

for i in range(n):
    for j in range(m):
        array_pad[i+3][j+3] = array[i][j]

def rotate_matrix_by_90(matrix):

    new_matrix = [[0] * len(matrix) for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[j][len(matrix)-i-1] = matrix[i][j]

    return new_matrix

def flip_matrix(matrix, d=1):

    new_matrix = [[0] * len(matrix) for _ in range(len(matrix))]

    if d == 1:

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_matrix[i][len(matrix)-j-1] = matrix[i][j]

        return new_matrix

    elif d == -1:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                new_matrix[len(matrix)-i-1][j] = matrix[i][j]

        return new_matrix

    else:
        return matrix

def get_score(kernel):

    max_score = 0
    for i in range(n+3):
        for j in range(m+3):
            value = 0
            possible = True
            for x in range(4):
                for y in range(4):
                    value += kernel[x][y] * array_pad[i+x][j+y]
                    if kernel[x][y] == 1 and array_pad[i+x][j+y] == 0:
                        possible = False
                        break
                if not possible:
                    value = 0
                    break
            max_score = max(max_score, value)
                    
    return max_score

kernel1 = [[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
kernel2 = [[0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0]]
kernel3 = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]]
kernel4 = [[0, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0]]
kernel5 = [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0]]

kernels = [kernel1, kernel2, kernel3, kernel4, kernel5]

result = 0
for kernel in kernels:
        
        for f in [0, -1, 1]:
            kernel = flip_matrix(kernel, d=f)
            for _ in range(4):
                kernel = rotate_matrix_by_90(kernel)

                result = max(result, get_score(kernel))

print(result)