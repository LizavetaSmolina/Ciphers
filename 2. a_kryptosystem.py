import math
# BSK - PS1
# Zadanie 2


def encrypt_matrix(input, d, key):
    _key = key.split("-")
    for i in range(len(_key)):
        _key[i] = int(_key[i])
    rows = math.ceil(len(input) / d)
    count = 0
    array = [[None for _ in range(d)] for _ in range(rows)]
    c = ''
    for i in range(rows):
        for j in range(d):
            if count < (len(input)):
                array[i][j] = input[count]
            count = count + 1
    for i in range(rows):
        for j in _key:
            if array[i][j - 1] is not None:
                c = c + str(array[i][j - 1])
            else:
                c = c + ' '
    return c


def decrypt_matrix(input, d, key):
    _key = key.split("-")
    for i in range(len(_key)):
        _key[i] = int(_key[i])
    _key.reverse()
    rows = math.ceil(len(input) / d)
    array = [[None for _ in range(d)] for _ in range(rows)]
    c = ''
    count = 0
    for i in range(rows):
        for j in range(d):
            if count < (len(input)):
                array[i][j] = input[count]
            count = count + 1
    for i in range(rows):
        for j in _key:
            if array[i][j - 1] is not None:
                c = c + str(array[i][j - 1])
    return c


if __name__ == "__main__":
    c = 'POLITECHNIKA'
    d = 5
    key = '3-4-1-5-2'
    print('Tekst do zakodowania: ', c)
    print('Klucz: ', key)
    print('Tekst zakodowany: ',encrypt_matrix(c, d, key))
    print('Tekst zdekodowany: ',decrypt_matrix(encrypt_matrix(c, d, key), d, key))
