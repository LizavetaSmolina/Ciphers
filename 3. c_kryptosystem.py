# BSK - PS1
# Zadanie 3
import math
import operator

 
def encrypt_matrix_c(input, key):
    d = {i: key[i] for i in range(len(key))}
    w = sorted(d.items(), key=operator.itemgetter(1))
    output = ''
    count = 0
    array = [[None for _ in range(len(key))] for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(w[i][0]+1):
            if count == len(input):
                break
            array[i][j] = input[count]
            count = count + 1
    for i in range(len(key)):
        column = w[i][0]
        for j in range(len(key)):
            if array[j][column] is not None:
                output = output + str(array[j][column])
    return output


if __name__ == "__main__":
    c = 'POLITECHNIKA'
    d = 'DZIEKAN'
    print('Tekst do zakodowania: ', c)
    print('Tekst zakodowany: ', encrypt_matrix_c(c, d))
