# BSK - PS1
# Zadanie 4
from string import ascii_uppercase as l


def search(char):
    for i in range(len(l)):
        if l[i] == char:
            return i
    return 0


def encrypt_caesar(input, k1, k0):
    n = len(l)
    output = ''
    for i in range(len(input)):
        output = output + l[(search(input[i]) * k1 + k0) % n]
    return output


def decrypt_caesar(input, k1, k0):
    n = len(l)
    output = ''
    for i in range(len(input)):
        z = 1
        for j in range(len(input)-1):
            z = (z * k1) % n
        v = (search(input[i]) + (n - k0)) * z
        ind = v % n
        if ind < 0: ind = ind + n
        output = output + l[ind]
    return output


if __name__ == "__main__":
    c = 'POLITECHNIKA'
    k0 = 7
    k1 = 3
    print('Tekst do zakodowania: ', c)
    print('Tekst zakodowany: ',encrypt_caesar(c, k1, k0))
    print('Tekst zdekodowany: ',decrypt_caesar(encrypt_caesar(c, k1, k0), k1, k0))
