import random


def fill_matrix(length, width):
    matrix = []
    for i in range(0, length):
        row = []
        for j in range(0, width):
            row.append(random.randint(0, 10))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            print(matrix[i][j], end=' ')
        print()
    print()


def matrix_transpos(matrix):
    new_matrix = []
    for i in range(0, len(matrix[0])):
        row = []
        for j in range(0, len(matrix)):
            row.append(matrix[j][i])
        new_matrix.append(row)
    return new_matrix


matrix = fill_matrix(3, 4)
print_matrix(matrix)
new_matrix = matrix_transpos(matrix)
print_matrix(new_matrix)
