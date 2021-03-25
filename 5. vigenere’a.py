# BSK - PS1
# Zadanie 5
from string import ascii_uppercase as l


def encrypt_vigenere(input, k):
    d = {l[i]: i for i in range(len(l))}
    vigenere_table = [l[i:] + l[:i] for i in range(len(l))]
    output = ''
    for i in range(len(input)):
        column = d.get(input[i])
        row = d.get(k[i])
        output = output + vigenere_table[row][column]
    return output


def decrypt_vigenere(input, k):
    d = {l[i]: i for i in range(len(l))}
    vigenere_table = [l[i:] + l[:i] for i in range(len(l))]
    output = ''
    for i in range(len(input)):
        column = d.get(k[i])
        for j in range(len(l)):
            if vigenere_table[j][column] == input[i]:
                row = j
                output = output + vigenere_table[0][j]
                break
    return output




if __name__ == "__main__":
   M = 'POLITECHNIKA'
   K = 'DZIEKANDZIEKAN'

   print('Tekst do zakodowania: ', M)
   print('Tekst zakodowany: ',encrypt_vigenere(M, K))
   print('Tekst zdekodowany: ', decrypt_vigenere(encrypt_vigenere(M, K), K))