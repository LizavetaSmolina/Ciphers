# BSK - PS1
# Zadanie 3
import math
import operator


def encrypt_matrix_b(input, key):
    d = {i: key[i] for i in range(len(key))}
    w = sorted(d.items(), key=operator.itemgetter(1))
    output = ''
    rows = math.ceil(len(input) / len(key))
    count = 0
    array = [[None for _ in range(len(key))] for _ in range(rows)]
    for i in range(rows):
        for j in range(len(key)):
            if count < (len(input)):
                array[i][j] = input[count]
            count = count + 1
    for i in range(len(key)):
        column = w[i][0]
        for j in range(rows):
            if array[j][column] is not None:
                output = output + str(array[j][column])
    return output


def decrypt_matrix_b(input, key):
    d = {i: key[i] for i in range(len(key))}
    w = sorted(d.items(), key=operator.itemgetter(1))
    output = ''
    rows = math.ceil(len(input) / len(key))
    rows_mod = len(input) % len(key)
    last_column = []
    for i in range(rows_mod):
        last_column.append(i)
    count = 0
    array = [[None for _ in range(len(key))] for _ in range(rows)]
    for i in range(len(key)):
         column = w[i][0]
         for j in range(rows):
             if column not in last_column and j == rows - 1: break
             if count == len(input): break
             array[j][column] = input[count]
             count = count + 1
    for i in range(rows):
        for j in range(len(key)):
            if array[i][j] is not None:
                output = output + str(array[i][j])
    return output


if __name__ == "__main__":
    c = 'POLITECHNIKA'
    d = 'DZIEKAN'
    print('Tekst do zakodowania: ', c)
    print('Tekst zakodowany: ',encrypt_matrix_b(c, d))
    print('Tekst zakodowany: ', decrypt_matrix_b(encrypt_matrix_b(c, d), d))